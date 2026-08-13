#!/bin/bash
# 托福口语系统 · 启动脚本（macOS 双击运行）
cd "$(dirname "$0")"

if curl -s --max-time 2 http://127.0.0.1:8765/health >/dev/null 2>&1; then
  echo "✓ 转写服务已在运行"
else
  export SSL_CERT_FILE="$(python3 -c 'import certifi; print(certifi.where())' 2>/dev/null)"
  nohup python3 transcribe_server.py > server.log 2>&1 &
  echo "✓ 正在启动语音转写服务（首次加载模型约需几秒）…"
  for i in $(seq 1 40); do
    sleep 1
    if curl -s --max-time 2 http://127.0.0.1:8765/health >/dev/null 2>&1; then
      echo "✓ 转写服务已就绪"
      break
    fi
  done
fi

open index.html
echo ""
echo "已打开口语系统主页（用 Chrome 打开效果最好）。"
echo "关闭此窗口不影响转写服务；要停止服务请双击 stop.command。"
