# Personal Knowledge System Skills

一套面向 Codex、兼容 Obsidian 与普通 Markdown 目录的个人知识库技能。

它覆盖建库访谈、Raw/Wiki/Outputs 架构、资料摄入、原子笔记、成长系统、Inspire Time、项目生命周期、复盘、自我观察和场景输出。每个技能可以单独安装，也可以通过 `$knowledge-vault` 进入完整流程。

## 快速开始

1. 将需要的目录从 `skills/` 复制到 Codex skills 目录，或先运行安装预览：

   ```powershell
   python -X utf8 scripts/install_codex_skills.py <codex-skills-directory> --dry-run
   python -X utf8 scripts/install_codex_skills.py <codex-skills-directory>
   ```

   第一次命令只显示计划；确认目标后再执行安装。
2. 重新打开一个 Codex 任务，让技能被发现。
3. 调用 `$knowledge-vault` 说明你想新建、整理或维护知识库。
4. 首次建库时，技能先访谈并展示写入预览；获得授权后才创建文件。

完整安装与用户路径见 [系统总览](docs/00-overview/system-overview.md) 和 [用户旅程](docs/00-overview/user-journey.md)。

## 技能

| Skill | 用途 |
|---|---|
| `knowledge-vault` | 总控入口、流程路由和基于证据的建议 |
| `vault-bootstrap` | 访谈后生成最小知识库 |
| `knowledge-intake` | 摄入资料并区分事实、判断、推测和冲突 |
| `atomic-notes` | 更新或创建可复用原子笔记 |
| `obsidian-vault` | Obsidian Properties、双链、Bases 和 Dashboard |
| `growth-system` | 候选、学习、能力、实践和优先级 |
| `inspire-time` | 将可迁移洞见变为实践 |
| `project-lifecycle` | 项目状态、决策、证据、中断恢复 |
| `retrospective` | 项目与周期复盘 |
| `self-observation` | 有证据、可反驳的自我观察 |
| `knowledge-output` | 按受众和披露边界生成输出 |

## 基本承诺

- 不把 AI 推测写成事实。
- 不因一次成功判定稳定能力。
- 不把输出稿反向当作事实来源。
- 不要求第三方 Obsidian 插件。
- 未获得写入授权时只提供提案和预览。
- 示例全部为虚构内容。

## 验证

```powershell
python -X utf8 scripts/validate_skill_structure.py
python -X utf8 scripts/validate_internal_links.py
python -X utf8 scripts/privacy_scan.py
```

详见 [验证与发布](docs/08-maintainers/validation-and-release.md)。
