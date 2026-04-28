<p align="center">
  <h1 align="center">Enreal AI Game Studio</h1>
  <p align="center">
    Turn a single AI coding session into a full game development studio.<br/>
    将单个 AI 编码会话升级为完整的游戏开发工作室。
    <br />
    49 agents. 72 skills. One coordinated AI team.<br/>
    49 个智能体，72 个技能，一个协同 AI 团队。
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href=".studio/agents"><img src="https://img.shields.io/badge/agents-49-blueviolet" alt="49 Agents"></a>
  <a href=".studio/skills"><img src="https://img.shields.io/badge/skills-72-green" alt="72 Skills"></a>
  <a href=".studio/hooks"><img src="https://img.shields.io/badge/hooks-12-orange" alt="12 Hooks"></a>
  <a href=".studio/rules"><img src="https://img.shields.io/badge/rules-11-red" alt="11 Rules"></a>
</p>

---

## Why This Exists
## 为什么会有这个项目

Building games with AI is powerful, but unstructured chat easily leads to messy code, weak design review, and missing QA.
使用 AI 做游戏很强大，但如果没有结构化流程，很容易出现代码混乱、设计缺乏评审、QA 缺失等问题。

**Enreal AI Game Studio** adds studio-style structure: directors, leads, specialists, quality gates, and reusable workflows.
**Enreal AI Game Studio** 提供“工作室级”结构：总监、负责人、专家分工、质量关卡和可复用工作流。

---

## What’s Included
## 包含内容

| Category | Description |
|---|---|
| Agents | 49 specialized agents across design/programming/art/audio/QA/production |
| Skills | 72 workflow skills for planning, implementation, review, testing, release |
| Hooks | 12 automation hooks for validation, logging, and safety checks |
| Rules | 11 path-scoped coding/design rules |
| Templates | 39 templates for docs, specs, plans, and reports |

| 类别 | 说明 |
|---|---|
| Agents | 49 个覆盖设计/程序/美术/音频/测试/制作的专业智能体 |
| Skills | 72 个用于规划、开发、评审、测试、发布的工作流技能 |
| Hooks | 12 个用于校验、日志与安全检查的自动化 Hook |
| Rules | 11 个按目录生效的代码/文档规范 |
| Templates | 39 个用于文档、规格、计划和报告的模板 |

---

## Getting Started
## 快速开始

### Prerequisites
### 环境要求

- Git
- Any coding AI client (OpenClaw / Codex CLI / Cursor / Windsurf / custom)
- Python 3.10+

- Git
- 任意编码 AI 客户端（OpenClaw / Codex CLI / Cursor / Windsurf / 自定义）
- Python 3.10+

### Setup
### 安装步骤

1. Clone repo  
   克隆仓库
```bash
git clone https://github.com/aldenpang/Enreal-AI-Game-Studio.git
cd Enreal-AI-Game-Studio
```

2. Configure providers  
   配置模型提供方
```bash
cp config/providers.example.yaml config/providers.yaml
# edit provider/model/base_url/api key env
```

3. Install runtime deps and run a skill  
   安装依赖并运行技能
```bash
pip install pyyaml openai
python scripts/run_skill.py start "I only have a rough game idea" --provider codex
python scripts/run_skill.py design-system "设计背包系统" --provider deepseek
python scripts/run_skill.py create-stories "将战斗系统拆成可开发故事" --provider gemma4_local
```

---

## Core Structure
## 核心目录结构

```text
STUDIO.md
.studio/
  agents/
  skills/
  hooks/
  rules/
  docs/
config/
scripts/
src/
design/
production/
```

`STUDIO.md` and `.studio/*` are the collaboration core.
`STUDIO.md` 与 `.studio/*` 是协作核心。

---

## How It Works
## 工作方式

- Vertical delegation: directors → leads → specialists.  
  纵向委派：总监 → 负责人 → 专家。
- Human-in-the-loop: ask → options → decision → draft → approval.  
  人类在环：提问 → 方案 → 决策 → 草稿 → 批准。
- Hooks and rules enforce consistency and safety automatically.  
  通过 Hooks 与规则自动保障一致性与安全性。

---

## Model-Agnostic Design
## 模型无关设计

This repo is provider-neutral and works with OpenAI-compatible APIs, including Codex-style models, DeepSeek, and local models via Ollama/vLLM.
本仓库是提供方中立设计，支持 OpenAI 兼容 API，包括 Codex 类模型、DeepSeek，以及通过 Ollama/vLLM 接入的本地模型。

---

## Community
## 社区

- Issues: <https://github.com/aldenpang/Enreal-AI-Game-Studio/issues>

- 问题反馈：<https://github.com/aldenpang/Enreal-AI-Game-Studio/issues>

---

## Acknowledgement
## 致谢

Special thanks to the original author and repository:
特别感谢原作者与原始项目：

- Donchitos — Claude Code Game Studios  
  <https://github.com/Donchitos/Claude-Code-Game-Studios>

This project is inspired by that work and adapted into a model-agnostic version.
本项目基于其思路进行二次改造，扩展为模型无关版本。

---

## License
## 许可证

MIT License. See [LICENSE](LICENSE).
MIT 许可证，详见 [LICENSE](LICENSE)。
