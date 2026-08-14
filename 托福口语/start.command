#!/bin/bash
# 托福口语系统 · 启动脚本（macOS 双击运行）
# 用固定 localhost 端口托管页面 + 转写，保证麦克风授权只需允许一次、永久记住。
cd "$(dirname "$0")"

# 每次启动都重启服务，确保加载最新代码（模型已缓存时秒开）
if curl -s --max-time 2 http://127.0.0.1:8765/health >/dev/null 2>&1; then
  lsof -ti :8765 | xargs kill 2>/dev/null
  sleep 1
fi

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

# 用固定 origin（127.0.0.1）打开，Chrome 会持久记住麦克风授权
URL="http://127.0.0.1:8765/"
if [ -d "/Applications/Google Chrome.app" ]; then
  open -a "Google Chrome" "$URL"
elif [ -d "/Applications/Microsoft Edge.app" ]; then
  open -a "Microsoft Edge" "$URL"
else
  open "$URL"
fi
echo ""
echo "已打开口语系统主页：$URL"
echo "首次录音点「允许」一次麦克风，之后自动记住，不再弹窗。"
echo "关闭此窗口不影响转写服务；要停止服务请双击 stop.command。"
