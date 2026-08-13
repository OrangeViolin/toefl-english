#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
托福口语 · 本地语音转写服务
接收浏览器录制的音频（webm/opus 等），用 faster-whisper 转写成英文文字。

用法：python3 transcribe_server.py   （监听 127.0.0.1:8765）
启动脚本见 start.command（双击即启动服务并打开浏览器）。
"""
import json
import os
import sys
import tempfile
import warnings
from http.server import BaseHTTPRequestHandler, HTTPServer

warnings.filterwarnings("ignore")

# 模型常驻内存（首次启动会从缓存/网络加载，之后复用）
MODEL_NAME = "base.en"
_model = None


def get_model():
    global _model
    if _model is None:
        from faster_whisper import WhisperModel
        # float32 在 Apple Silicon 上稳且快；模型已缓存时加载 <1s
        _model = WhisperModel(MODEL_NAME, device="cpu", compute_type="float32")
    return _model


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"ok": True, "model": MODEL_NAME}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self._cors()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self._cors()
            self.end_headers()

    def do_POST(self):
        if self.path != "/transcribe":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)
        if not data:
            self._respond(400, {"error": "空音频"})
            return
        tmp = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as f:
                f.write(data)
                tmp = f.name
            model = get_model()
            segments, info = model.transcribe(tmp, language="en", beam_size=5, vad_filter=True)
            text = "".join(s.text for s in segments).strip()
            self._respond(200, {"text": text})
        except Exception as e:
            self._respond(500, {"error": str(e)})
        finally:
            if tmp and os.path.exists(tmp):
                try:
                    os.unlink(tmp)
                except OSError:
                    pass

    def _respond(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self._cors()
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # 静默，避免刷屏


def main():
    port = 8765
    # 预加载模型（首次可能需下载，给用户明确提示）
    print(f"正在加载语音识别模型 {MODEL_NAME}（首次可能下载，之后秒开）…", flush=True)
    get_model()
    print(f"✓ 转写服务已就绪：http://127.0.0.1:{port}/transcribe", flush=True)
    try:
        HTTPServer(("127.0.0.1", port), Handler).serve_forever()
    except OSError as e:
        print(f"✗ 端口 {port} 被占用（服务可能已在运行？）：{e}", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
