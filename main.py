#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zero Team Engine - CLI Tools
"""

import sys
from pathlib import Path

def list_agents():
    """列出所有 Agent"""
    print("=== Zero Team Engine Agents ===")
    print("CEO         - 首席执行官")
    print("Engineer    - 工程师")
    print("Designer    - 设计师")
    print("Frontend    - 前端设计")
    print("Game UI     - 游戏UI")
    print("Researcher  - 研究员")
    print("QA          - 测试")
    print("DevOps      - 运维")
    print("PM          - 产品经理")

def show_status():
    """显示系统状态"""
    print("=== System Status ===")
    print("Memory: Ready")
    print("Evaluation: Ready")
    print("Evolution: Ready")

def main():
    if len(sys.argv) < 2:
        print("Zero Team Engine CLI")
        print("")
        print("Usage:")
        print("  python main.py agents     # 列出所有 Agent")
        print("  python main.py status     # 显示系统状态")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "agents":
        list_agents()
    elif cmd == "status":
        show_status()

if __name__ == "__main__":
    main()