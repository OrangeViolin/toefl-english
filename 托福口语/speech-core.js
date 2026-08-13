/* 托福口语系统 · 录音 + 语音转写 + TTS 核心
 * 录音 → 本地 faster-whisper 服务转写（准），服务不可用时回退 Web Speech API
 * 依赖：Chrome / Edge（MediaRecorder + getUserMedia）
 * 全局暴露 window.VocaSpeech
 */
(function () {
  'use strict';

  // ---------- TTS（美式女声朗读）----------
  let ttsVoice = null;
  const PREF = ['Google US English', 'Microsoft Aria', 'Microsoft Jenny', 'Microsoft Ava',
    'Samantha', 'Ava', 'Allison', 'Susan', 'Zoe', 'Karen', 'Victoria'];
  function pickVoice() {
    try {
      const vs = speechSynthesis.getVoices() || [];
      let us = vs.filter(v => /en[-_]US/i.test(v.lang) || /United States/i.test(v.name));
      if (!us.length) us = vs.filter(v => /^en/i.test(v.lang));
      for (const n of PREF) {
        const h = us.find(v => v.name === n) || us.find(v => v.name.indexOf(n) === 0);
        if (h) { ttsVoice = h; return; }
      }
      ttsVoice = us.find(v => /samantha|google us|female|ava|zoe|karen|allison|susan/i.test(v.name)) || us[0] || vs[0] || null;
    } catch (e) { }
  }
  if ('speechSynthesis' in window) {
    if ('onvoiceschanged' in speechSynthesis) speechSynthesis.onvoiceschanged = pickVoice;
    pickVoice();
  }

  function say(text) {
    return new Promise(res => {
      if (!('speechSynthesis' in window)) { res(false); return; }
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US'; if (ttsVoice) u.voice = ttsVoice; u.rate = 0.9; u.pitch = 1;
      let done = false;
      u.onend = () => { if (!done) { done = true; res(true); } };
      u.onerror = () => { if (!done) { done = true; res(false); } };
      speechSynthesis.speak(u);
    });
  }
  function stopTts() { if ('speechSynthesis' in window) speechSynthesis.cancel(); }

  // ---------- 录音 + 转写 ----------
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  const WHISPER_URL = 'http://127.0.0.1:8765/transcribe';
  const supported = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder);

  let mediaStream = null, recorder = null, chunks = [], recognition = null;
  let active = false, startTime = 0;
  let webText = '';   // Web Speech API 备胎的转写结果

  function clean(s) { return (s || '').replace(/\s+/g, ' ').trim(); }

  // 探测 whisper 服务是否在跑（供 UI 提示）
  function checkServer() {
    return fetch('http://127.0.0.1:8765/health', { signal: AbortSignal.timeout(2500) })
      .then(r => r.ok).catch(() => false);
  }

  function start(onStatus) {
    return new Promise(async (resolve, reject) => {
      try {
        stopTts();
        if (!mediaStream || mediaStream.getTracks().every(t => t.readyState === 'ended')) {
          mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        }
      } catch (e) {
        reject(new Error('无法访问麦克风：' + e.message + '（请用 Chrome 打开，并允许麦克风权限）'));
        return;
      }
      chunks = []; webText = '';
      try { recorder = new MediaRecorder(mediaStream); }
      catch (e) { reject(new Error('浏览器不支持 MediaRecorder，请用 Chrome')); return; }
      recorder.ondataavailable = e => { if (e.data && e.data.size) chunks.push(e.data); };
      recorder.start();

      // 后台跑 Web Speech API 作为备胎（录音时不显示实时结果，只在 whisper 不可用时兜底）
      if (SR) {
        try {
          recognition = new SR();
          recognition.lang = 'en-US';
          recognition.continuous = true;
          recognition.interimResults = false;
          recognition.onresult = e => {
            let fin = '';
            for (let i = 0; i < e.results.length; i++) if (e.results[i].isFinal) fin += e.results[i][0].transcript;
            if (fin) webText += fin;
          };
          recognition.onerror = () => { };
          recognition.onend = () => {
            if (active && recognition && !recognition._stopped) { try { recognition.start(); } catch (_) { } }
          };
          recognition.start();
        } catch (e) { recognition = null; }
      }
      active = true; startTime = Date.now();
      if (onStatus) onStatus('recording');
      resolve();
    });
  }

  function stop(onStatus) {
    return new Promise(resolve => {
      active = false;
      const duration = (Date.now() - startTime) / 1000;
      if (recognition) { try { recognition._stopped = true; recognition.stop(); } catch (_) { } recognition = null; }
      let blob = null, url = null;
      if (recorder && recorder.state !== 'inactive') {
        recorder.onstop = () => {
          blob = new Blob(chunks, { type: 'audio/webm' });
          url = URL.createObjectURL(blob);
        };
        try { recorder.stop(); } catch (_) { }
      }
      setTimeout(async () => {
        if (mediaStream) { /* 保留 stream 复用，不释放 */ }
        recorder = null; chunks = [];
        if (onStatus) onStatus('transcribing');
        let text = '', engine = 'web';
        // 1) 优先本地 whisper（准）
        if (blob) {
          const w = await transcribeWhisper(blob);
          if (w !== null) { text = w; engine = 'whisper'; }
        }
        // 2) 回退 Web Speech API
        if (!text) text = clean(webText);
        resolve({ transcript: clean(text), engine, blob, url, duration });
      }, 450);
    });
  }

  async function transcribeWhisper(blob) {
    try {
      const ctrl = new AbortController();
      const t = setTimeout(() => ctrl.abort(), 20000);
      const r = await fetch(WHISPER_URL, { method: 'POST', body: blob, signal: ctrl.signal });
      clearTimeout(t);
      if (!r.ok) return null;
      const j = await r.json();
      return (j && typeof j.text === 'string') ? j.text : null;
    } catch (e) { return null; }
  }

  function release() {
    if (mediaStream) { mediaStream.getTracks().forEach(t => t.stop()); mediaStream = null; }
    active = false;
  }
  if (typeof window !== 'undefined') window.addEventListener('beforeunload', release);

  window.VocaSpeech = { supported, say, stopTts, start, stop, checkServer, release, pickVoice };
})();
