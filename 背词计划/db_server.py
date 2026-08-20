#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""背词计划 · 掌握数据云端库（cloud.db）
把「掌握/未掌握」标记持久化到 SQLite 文件 cloud.db，页面每次改动即写库、加载即读库——
localStorage 被清也能从 cloud.db 恢复，绝不再丢。

用法：  python3 db_server.py     (或双击 start.command)
        然后浏览器打开 http://127.0.0.1:8799/  (由本服务托管 index.html)
接口：  GET /state           -> {key:'ok'|'no', ...}         读取全部标记
        POST /mark {k,status}-> 单个 upsert；status 非 ok/no 则删除该键
        POST /bulk {items}   -> 批量 upsert（只增不删，用于把本地标记同步上云、导入）
        GET /health          -> {ok,count}
数据文件：背词计划/cloud.db（可随项目一起 git 备份/同步）
"""
import json, os, sqlite3, time, http.server, socketserver
from urllib.parse import urlparse

BASE = os.path.dirname(os.path.abspath(__file__))
DBF  = os.path.join(BASE, "cloud.db")
HTML = os.path.join(BASE, "index.html")
PORT = 8799

def db():
    c = sqlite3.connect(DBF)
    c.execute("CREATE TABLE IF NOT EXISTS mastery(k TEXT PRIMARY KEY, status TEXT, updated INTEGER)")
    return c

class H(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()
    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code); self.send_header("Content-Type", "application/json; charset=utf-8")
        self._cors(); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        p = urlparse(self.path).path
        if p in ("/", "/index.html"):
            try:
                with open(HTML, "rb") as f: b = f.read()
                self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-store"); self._cors()
                self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
            except Exception:
                self._json({"error": "index.html 缺失，先跑 python3 build.py"}, 500)
            return
        if p == "/state":
            c = db(); rows = c.execute("SELECT k,status FROM mastery").fetchall(); c.close()
            return self._json({k: s for k, s in rows if s})
        if p == "/health":
            c = db(); n = c.execute("SELECT COUNT(*) FROM mastery").fetchone()[0]; c.close()
            return self._json({"ok": True, "count": n, "db": DBF})
        self._json({"error": "not found"}, 404)
    def do_POST(self):
        p = urlparse(self.path).path
        ln = int(self.headers.get("Content-Length", 0)); body = self.rfile.read(ln) if ln else b"{}"
        try: data = json.loads(body or b"{}")
        except Exception: return self._json({"error": "bad json"}, 400)
        c = db(); now = int(time.time())
        if p == "/mark":
            k = data.get("k"); st = data.get("status")
            if k:
                if st in ("ok", "no"):
                    c.execute("INSERT INTO mastery(k,status,updated) VALUES(?,?,?) ON CONFLICT(k) DO UPDATE SET status=excluded.status,updated=excluded.updated", (k, st, now))
                else:
                    c.execute("DELETE FROM mastery WHERE k=?", (k,))
                c.commit()
            c.close(); return self._json({"ok": True})
        if p == "/bulk":
            items = data.get("items", {}) or {}
            n = 0
            for k, st in items.items():
                if st in ("ok", "no"):
                    c.execute("INSERT INTO mastery(k,status,updated) VALUES(?,?,?) ON CONFLICT(k) DO UPDATE SET status=excluded.status,updated=excluded.updated", (k, st, now)); n += 1
            c.commit(); c.close(); return self._json({"ok": True, "n": n})
        c.close(); self._json({"error": "not found"}, 404)
    def log_message(self, *a): pass

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), H) as s:
        c = db(); n = c.execute("SELECT COUNT(*) FROM mastery").fetchone()[0]; c.close()
        print(f"背词 cloud.db 已启动 → http://127.0.0.1:{PORT}/   现有标记 {n} 条   db: {DBF}")
        s.serve_forever()
