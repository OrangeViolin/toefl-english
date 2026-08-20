#!/bin/bash
# 背词计划 · 启动云端库并打开页面（掌握/未掌握持久化到 cloud.db，绝不再丢）
cd "$(dirname "$0")"
# 已在跑就不重复起
if ! lsof -i :8799 >/dev/null 2>&1; then
  nohup python3 db_server.py >/tmp/bici_db_server.log 2>&1 &
  sleep 1
fi
open "http://127.0.0.1:8799/"
