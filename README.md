<!-- ZERO TEAM ENGINE -->

<div align="center">
  <img src="images/logo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Zero Team Engine</h3>
  <p align="center">
    AI 一人公司运营系统 | AI One-Person Company Operating System
    <br />
    <a href="https://github.com/quick123-666/Zero-Team-Engine"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/quick123-666/Zero-Team-Engine/releases/latest">
      <img src="https://img.shields.io/github/v/release/quick123-666/Zero-Team-Engine?style=flat-square" alt="Version">
    </a>
    <a href="https://github.com/quick123-666/Zero-Team-Engine/issues">
      <img src="https://img.shields.io/github/issues/quick123-666/Zero-Team-Engine?style=flat-square" alt="Issues">
    </a>
    <a href="https://github.com/quick123-666/Zero-Team-Engine/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/quick123-666/Zero-Team-Engine?style=flat-square" alt="License">
    </a>
    <a href="https://github.com/quick123-666/Zero-Team-Engine/stargazers">
      <img src="https://img.shields.io/github/stars/quick123-666/Zero-Team-Engine?style=flat-square" alt="Stars">
    </a>
    <a href="https://github.com/quick123-666/Zero-Team-Engine/network/members">
      <img src="https://img.shields.io/github/forks/quick123-666/Zero-Team-Engine?style=flat-square" alt="Forks">
    </a>
  </p>
</div>

> English | [中文](#chinese)

<a name="english"></a>

## About The Project

Zero Team Engine 是一个用于运营 AI 一人公司的综合系统。它充当虚拟首席执行官 (CEO)，管理多个专业 AI Agent，包括 Engineer、Designer、Frontend、Researcher 等，实现自动化公司运营。

### Features

- **多 Agent 协作系统** - CEO 管理多个专业 Agent
- **记忆系统** - 自动保存任务和对话历史
- **评分系统** - 5 维度评估 Agent 表现
- **自进化机制** - 根据评分自动优化配置
- **游戏风格控制面板** - RPG 主题 UI

### 为什么选择 Zero Team Engine?

- 🤖 自动化运营 - 无需人工干预
- 📊 数据驱动 - 基于评分的决策
- 🔄 自我优化 - 持续学习和进化
- 🎮 游戏化体验 - 直观的管理界面

### Built With

- [Python 3.8+](https://www.python.org/)
- [OpenCode](https://opencode.ai/)
- HTML/CSS/JavaScript

---

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository
```bash
git clone https://github.com/quick123-666/Zero-Team-Engine.git
cd Zero-Team-Engine
```

2. Explore the project
```bash
# Open control-panel.html in browser
start control-panel.html
```

### Quick Start

```bash
# List all Agents
python agents/list.py

# Check system status
python system/status.py
```

---

## Project Structure

```
Zero-Team-Engine/
├── README.md           # This file
├── LICENSE             # MIT License
├── control-panel.html  # Game-style dashboard
├── agents/             # Agent definitions
│   ├── ceo.md         # CEO role
│   ├── engineer.md   # Engineer role
│   ├── designer.md   # Designer role
│   └── ...
├── memory/             # Memory system
├── evaluation/         # Scoring system
├── evolution/         # Self-evolution
├── docs/               # Documentation
└── skills/            # Skills directory
```

---

## Core Modules

### 1. Agent System

| Agent | Role | Status |
|-------|------|--------|
| CEO | 首席执行官 | ✅ |
| Engineer | 工程师 | ✅ |
| Designer | 设计师 | ✅ |
| Frontend | 前端设计 | ✅ |
| Game UI | 游戏UI | ✅ |
| Researcher | 研究员 | ✅ |
| QA | 测试 | ✅ |
| DevOps | 运维 | ✅ |
| PM | 产品经理 | ✅ |

### 2. Memory System

自动保存任务结果和对话历史，支持查询和检索。

```bash
python memory.py save CEO T001 "任务结果"
python memory.py query CEO
```

### 3. Scoring System

5 维度评估: 质量(30%)、速度(25%)、成本(20%)、协作(15%)、创新(10%)

```bash
python score.py rate Researcher T001 85 90 80 75 70
python score.py leaderboard
```

### 4. Self-Evolution

根据评分自动优化配置，安装新技能。

```bash
python evolution.py check
```

---

## Control Panel

Open `control-panel.html` in browser to access the game-style dashboard with:

- **总览 (Dashboard)** - Overview statistics
- **Agent** - Agent management
- **任务 (Tasks)** - Task queue
- **成本 (Cost)** - Cost analysis
- **评分 (Score)** - Scoring system
- **进化 (Evolution)** - Self-evolution

---

## Contributing

Contributions are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License.

---

## Acknowledgments

- [OpenCode](https://opencode.ai/) - AI coding assistant
- Claude Code / Claude API
- All contributors

---

<a name="chinese"></a>

## 中文说明

### 关于项目

Zero Team Engine 是一个用于运营 AI 一人公司的综合系统。它充当虚拟首席执行官 (CEO)，管理多个专业 AI Agent，包括工程师、设计师、研究员等，实现自动化公司运营。

### 核心功能

- **多 Agent 协作** - 10 个专业 Agent 分工协作
- **记忆系统** - 自动存档和查询
- **评分系统** - 5 维度评估表现
- **自进化** - 根据评分自动优化

### 快速开始

```bash
# 打开控制面板
start control-panel.html

# 查看 Agent 列表
python agents/list.py
```

### 系统架构

| 模块 | 功能 |
|------|------|
| agents/ | 10 个 Agent 角色定义 |
| memory/ | 记忆存档系统 |
| evaluation/ | 评分系统 |
| evolution/ | 自进化机制 |

### 控制面板

- 游戏风格 RPG 主题 UI
- Tab 切换: 总览/Agent/任务/成本/评分/进化

---

<div align="center">
  Made with ❤️ by Zero Team Engine
</div>

[(Back to top)](#english)