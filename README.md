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

Zero Team Engine is a comprehensive system for operating an AI-powered one-person company. It acts as a virtual CEO, managing multiple specialized AI Agents including Engineers, Designers, Researchers, and more, enabling fully automated company operations.

### Features

- **Multi-Agent Collaboration** - 10 specialized Agents working together
- **Memory System** - Auto-save task results and conversation history
- **Scoring System** - 5-dimension evaluation (Quality/Speed/Cost/Collaboration/Innovation)
- **Self-Evolution** - Auto-optimize based on scores
- **Game-Style Dashboard** - RPG-themed control panel

### Why Zero Team Engine?

- 🤖 Automated Operations - No human intervention needed
- 📊 Data-Driven - Score-based decision making
- 🔄 Self-Optimizing - Continuous learning and evolution
- 🎮 Gamified Experience - Intuitive management interface

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

2. Open control panel
```bash
# Simply open control-panel.html in browser
start control-panel.html
```

3. Or use CLI
```bash
python main.py agents
python main.py status
```

---

## Project Structure

```
Zero-Team-Engine/
├── README.md           # This file
├── LICENSE           # MIT License
├── main.py           # CLI tools
├── control-panel.html # Game-style dashboard
├── agents/          # Agent definitions
├── memory/          # Memory system
├── evaluation/      # Scoring system
├── evolution/       # Self-evolution
└── docs/           # Documentation
```

---

## Core Modules

### 1. Agent System

| Agent | Role | Status |
|-------|------|--------|
| CEO | Chief Executive Officer | ✅ |
| Engineer | Engineer | ✅ |
| Designer | Designer | ✅ |
| Frontend | Frontend Dev | ✅ |
| Game UI | Game UI Designer | ✅ |
| Researcher | Researcher | ✅ |
| QA | Quality Assurance | ✅ |
| DevOps | DevOps | ✅ |
| PM | Product Manager | ✅ |

### 2. Memory System

Auto-save tasks and conversation history with query support.

```bash
python memory.py save CEO T001 "Task result"
python memory.py query CEO
```

### 3. Scoring System

5-dimension evaluation: Quality(30%), Speed(25%), Cost(20%), Collaboration(15%), Innovation(10%)

```bash
python score.py rate Researcher T001 85 90 80 75 70
python score.py leaderboard
```

### 4. Self-Evolution

Auto-optimize configuration based on scores.

```bash
python evolution.py check
```

---

## Dashboard

Open `control-panel.html` in browser to access the game-style RPG-themed dashboard:

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

Distributed under the MIT License. See `LICENSE` for more information.

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
- **评分系统** - 5 维度评估 (质量/速度/成本/协作/创新)
- **自进化** - 根据评分自动优化配置

### 为什么选择 Zero Team Engine?

- 🤖 自动化运营 - 无需人工干预
- 📊 数据驱动 - 基于评分的决策
- 🔄 自我优化 - 持续学习和进化
- 🎮 游戏化体验 - 直观的管理界面

### 快速开始

```bash
# 克隆项目
git clone https://github.com/quick123-666/Zero-Team-Engine.git
cd Zero-Team-Engine

# 用浏览器打开控制面板
start control-panel.html

# 或使用命令行
python main.py agents
python main.py status
```

### 系统架构

| 模块 | 功能 |
|------|------|
| agents/ | 10 个 Agent 角色定义 |
| memory/ | 记忆存档系统 |
| evaluation/ | 评分系统 |
| evolution/ | 自进化机制 |

### Agent 列表

| Agent | 角色 | 状态 |
|-------|------|------|
| CEO | 首席执行官 | ✅ |
| Engineer | 工程师 | ✅ |
| Designer | 设计师 | ✅ |
| Frontend | 前端设计 | ✅ |
| Game UI | 游戏UI | ✅ |
| Researcher | 研究员 | ✅ |
| QA | 测试 | ✅ |
| DevOps | 运维 | ✅ |
| PM | 产品经理 | ✅ |

### 控制面板

- 游戏风格 RPG 主题 UI
- Tab 切换: 总览/Agent/任务/成本/评分/进化

### 贡献

欢迎贡献！

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 许可证

MIT 许可证 -详见 LICENSE 文件。

---

<div align="center">
  Made with ❤️ by Zero Team Engine
</div>

[(Back to top)](#english)