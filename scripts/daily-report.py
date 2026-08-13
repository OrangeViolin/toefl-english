#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""根据 git commit 历史自动生成每日工作报告。

读取当前仓库的 commit 历史，按作者提交日期分组，为每个有 commit 的日期
生成一份 Markdown 工作报告，写入仓库根目录下的「工作报告/」子文件夹。

工作报告文件夹不纳入 git 版本管理（见 .gitignore），由本脚本全量重建，
因此无论何时运行，报告内容都会与 git 历史保持一致。

用法：
    python3 scripts/daily-report.py            # 全量重建所有日期的报告（幂等）
    python3 scripts/daily-report.py --today    # 只重建今天的报告
"""

import os
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

REPORT_DIR_NAME = "工作报告"


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8").stdout


def repo_root():
    out = run(["git", "rev-parse", "--show-toplevel"]).strip()
    if not out:
        sys.exit("错误：当前不在 git 仓库内。")
    return Path(out)


def parse_commits():
    """返回 { 'YYYY-MM-DD': [commit, ...] }，commit 按时间正序。"""
    fmt = "%H%x1f%ad%x1f%an%x1f%s%x1f%b%x1e"
    log = run(
        [
            "git", "log", "--reverse",
            "--date=format:%Y-%m-%d %H:%M:%S",
            "--pretty=format:" + fmt,
        ]
    )
    by_day = defaultdict(list)
    for record in log.split("\x1e"):
        record = record.strip()
        if not record:
            continue
        fields = record.split("\x1f")
        if len(fields) < 4:
            continue
        h, adate, aname, subject = fields[0], fields[1], fields[2], fields[3]
        body = fields[4] if len(fields) > 4 else ""
        # 过滤 Co-Authored-By 等自动追加行，让报告只保留人类撰写的内容
        body = "\n".join(
            line for line in body.splitlines()
            if not line.strip().startswith("Co-Authored-By:")
        ).strip()
        files = run(
            ["git", "-c", "core.quotepath=false", "diff-tree",
             "--no-commit-id", "--name-only", "-r", "--root", h]
        ).strip().splitlines()
        day = adate[:10] if len(adate) >= 10 else adate
        by_day[day].append({
            "hash": h[:7],
            "time": adate[11:16] if len(adate) >= 16 else adate,
            "author": aname,
            "subject": subject,
            "body": body.strip(),
            "files": files,
        })
    return by_day


def render_day(day, commits, generated_at):
    lines = [f"# 工作报告 · {day}", ""]
    lines.append(f"> 共 {len(commits)} 次提交 · 由 daily-report.py 自动生成于 {generated_at}")
    lines.append("")
    for c in commits:
        lines.append(f"## {c['time']} · {c['subject']}")
        lines.append("")
        lines.append(f"- **提交** `{c['hash']}` · {c['author']}")
        if c["body"]:
            lines.append("")
            lines.append(c["body"])
        if c["files"]:
            lines.append("")
            lines.append("**变更文件**")
            lines.append("")
            for f in c["files"]:
                lines.append(f"- `{f}`")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    root = repo_root()
    os.chdir(root)

    by_day = parse_commits()
    if not by_day:
        print("没有可汇总的 commit。")
        return 0

    report_dir = root / REPORT_DIR_NAME
    report_dir.mkdir(exist_ok=True)

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    only_today = "--today" in sys.argv
    today = date.today().isoformat()

    for day in sorted(by_day):
        if only_today and day != today:
            continue
        path = report_dir / f"{day}.md"
        path.write_text(render_day(day, by_day[day], generated_at), encoding="utf-8")
        print(f"已生成 {path.relative_to(root)}（{len(by_day[day])} 次提交）")

    return 0


if __name__ == "__main__":
    sys.exit(main())
