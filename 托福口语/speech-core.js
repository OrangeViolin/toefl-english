/* 托福口语系统 · 录音 + 语音转写 + TTS 核心
 * 依赖：Chrome / Edge（Web Speech API + MediaRecorder + getUserMedia）
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

  // ---------- 录音 + 语音转写 ----------
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  const supported = !!SR && !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);

  let mediaStream = null, recorder = null, chunks = [], recognition = null;
  let active = false, startTime = 0, finalText = '', interimText = '', onUpdateCb = null;

  function clean(s) { return (s || '').replace(/\s+/g, ' ').trim(); }

  function start(onUpdate) {
    return new Promise(async (resolve, reject) => {
      try {
        stopTts();
        mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
      } catch (e) {
        reject(new Error('无法访问麦克风：' + e.message + '（请用 Chrome 打开，并允许麦克风权限）'));
        return;
      }
      chunks = []; finalText = ''; interimText = ''; onUpdateCb = onUpdate || null;
      try {
        recorder = new MediaRecorder(mediaStream);
      } catch (e) { reject(new Error('浏览器不支持 MediaRecorder，请用 Chrome')); return; }
      recorder.ondataavailable = e => { if (e.data && e.data.size) chunks.push(e.data); };
      recorder.start();

      if (SR) {
        try {
          recognition = new SR();
          recognition.lang = 'en-US';
          recognition.continuous = true;
          recognition.interimResults = true;
          recognition.onresult = e => {
            let fin = '';
            for (let i = 0; i < e.results.length; i++) {
              const r = e.results[i];
              if (r.isFinal) fin += r[0].transcript;
              else interimText = r[0].transcript;
            }
            if (fin) finalText += fin;
            if (onUpdateCb) onUpdateCb(clean(finalText), clean(interimText));
          };
          recognition.onerror = e => { console.warn('SR error', e.error); };
          recognition.onend = () => {
            if (active && recognition && !recognition._stopped) {
              try { recognition.start(); } catch (_) { }
            }
          };
          recognition.start();
        } catch (e) { console.warn('SpeechRecognition start failed', e); recognition = null; }
      }
      active = true; startTime = Date.now();
      resolve();
    });
  }

  function stop() {
    return new Promise(resolve => {
      active = false;
      const duration = (Date.now() - startTime) / 1000;
      if (recognition) {
        try { recognition._stopped = true; recognition.stop(); } catch (_) { }
        recognition = null;
      }
      let blob = null, url = null;
      if (recorder && recorder.state !== 'inactive') {
        recorder.onstop = () => {
          blob = new Blob(chunks, { type: 'audio/webm' });
          url = URL.createObjectURL(blob);
        };
        try { recorder.stop(); } catch (_) { }
      }
      // 等 400ms 让 SpeechRecognition 把最后的 interim 结果 flush 成 final，再收尾
      setTimeout(() => {
        if (mediaStream) { mediaStream.getTracks().forEach(t => t.stop()); mediaStream = null; }
        recorder = null; chunks = [];
        resolve({ transcript: clean(finalText), blob, url, duration });
      }, 400);
    });
  }

  window.VocaSpeech = { supported, say, stopTts, start, stop, pickVoice };
})();
