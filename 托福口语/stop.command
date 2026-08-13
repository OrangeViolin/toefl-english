#!/bin/bash
# 托福口语系统 · 停止转写服务
lsof -ti :8765 | xargs kill 2>/dev/null && echo "✓ 转写服务已停止" || echo "服务未在运行"
