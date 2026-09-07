# 通用规则映射

本表用于确认方法已分类进入公开结构。它只描述通用问题，不保存任何真实用户内容。

| 方法类别 | 大众化规则 | 主要 Skill | 主要文档 | 验证场景 |
|---|---|---|---|---|
| 三层架构 | 原始证据、维护知识、场景输出分层 | vault-bootstrap | docs/01-architecture/raw-wiki-outputs.md | bootstrap |
| 暂存与归类 | 低风险未知项进入 Inbox，重要判断请求确认 | knowledge-intake | docs/03-knowledge-workflows/information-intake.md | intake |
| 导航职责 | Home、Dashboard、Index 分别处理入口、当前状态、领域检索 | obsidian-vault | docs/01-architecture/links-and-indexes.md | bootstrap |
| 最小建库 | 访谈后按需生成，不预建完整人生分类 | vault-bootstrap | docs/02-onboarding/minimum-vault-generation.md | bootstrap |
| 隐私授权 | 读取、写入、披露分别确认 | knowledge-vault | docs/02-onboarding/privacy-and-disclosure.md | output |
| 陈述状态 | 事实、自述、判断、推测、冲突分别标注 | knowledge-intake | docs/03-knowledge-workflows/fact-inference-and-conflict.md | intake |
| 来源追溯 | 来源靠近陈述，AI 整理不作为来源 | knowledge-intake | docs/03-knowledge-workflows/source-traceability.md | intake |
| 更新优先 | 搜索标题、别名、关键词和语义邻居后再创建 | atomic-notes | docs/03-knowledge-workflows/update-before-create.md | atomic-note |
| 原子性 | 一个可独立维护的可复用问题或结论 | atomic-notes | docs/03-knowledge-workflows/atomic-notes.md | atomic-note |
| 强关系链接 | 只链接来源、主题、依赖和真实应用 | atomic-notes | docs/01-architecture/links-and-indexes.md | atomic-note |
| 生命周期 | 状态、复查日期、替代关系和归档原因可追溯 | obsidian-vault | docs/01-architecture/freshness-and-archiving.md | bootstrap |
| 候选机制 | 新兴趣先评估，确认后才进入正式池 | growth-system | docs/04-growth-and-learning/candidate-to-commitment.md | growth review |
| 资源与能力 | 内容消费不是掌握证明 | growth-system | docs/04-growth-and-learning/learning-resources.md | growth review |
| 掌握证据 | 解释、应用、异常处理和迁移逐级记录 | growth-system | docs/04-growth-and-learning/practice-and-evidence.md | growth review |
| 容量控制 | 限制同期重点并保留恢复空间 | growth-system | docs/04-growth-and-learning/priority-and-capacity.md | growth review |
| Inspire Time | 可迁移洞见连接一个现实实践 | inspire-time | docs/04-growth-and-learning/inspire-time.md | inspire-time |
| 项目启动 | 目标、完成标准、范围、约束和下一步明确 | project-lifecycle | docs/05-projects-and-reviews/project-lifecycle.md | project review |
| 项目决策 | 选项、依据、代价、验证和回退条件分开 | project-lifecycle | docs/05-projects-and-reviews/project-status-and-decisions.md | project review |
| 中断恢复 | 从真实状态接续，不重复已完成工作 | project-lifecycle | skills/project-lifecycle/references/interruption-and-resume.md | project review |
| 能力归属 | 区分用户、团队、工具和 AI 的贡献 | project-lifecycle | docs/05-projects-and-reviews/capability-evidence.md | retrospective |
| 项目复盘 | 总结事实，复盘判断与改变 | retrospective | docs/05-projects-and-reviews/project-retrospective.md | retrospective |
| 周期复盘 | 事件持续记录，周期生成截止快照 | retrospective | docs/05-projects-and-reviews/event-log-and-time-snapshots.md | retrospective |
| 自我观察 | 证据、推测、置信度、其他解释、反例分开 | self-observation | docs/06-self-knowledge/evidence-based-observation.md | self-observation |
| 个人说明书 | 待验证观察积累后形成低频修订提案 | self-observation | docs/06-self-knowledge/revision-cycle.md | self-observation |
| Obsidian 属性 | YAML 合法、字段稳定、核心信息可迁移 | obsidian-vault | docs/07-obsidian/properties.md | structure validation |
| Bases | 数据留在笔记，Base 只提供视图 | obsidian-vault | docs/07-obsidian/bases.md | structure validation |
| 对外输出 | 先明确受众、目的、披露、来源版本和审核 | knowledge-output | docs/03-knowledge-workflows/knowledge-output.md | output |
| 建议 | 基于目标和证据提供选项、权衡与小验证 | knowledge-vault | skills/knowledge-vault/references/advice-protocol.md | orchestrator review |
| 系统变更 | 先改规范和模板，再迁移内容并保留恢复路径 | knowledge-vault | docs/01-architecture/freshness-and-archiving.md | maintainer review |

