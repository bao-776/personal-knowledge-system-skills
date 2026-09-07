# Personal Knowledge System Skills

一套可以在 Codex 中调用、兼容 Obsidian 与普通 Markdown 文件夹的个人知识库 Skill。

我想做的并不只是一个“把资料放整齐”的工具。我们每天接触的信息越来越多：工作中的项目，科研里的问题，学过的课程，突然闪过的念头，还有那些当时很重要、后来却想不起来的感受和判断。它们不该都压在脑子里，也不该只是被丢进一个越来越满的收藏夹。

我希望这套 Skill 能陪你把零散的信息慢慢变成自己的理解：知道它从哪里来，和什么有关，在哪一次行动中真正用过，又怎样改变了你。让知识库替你承担一部分记忆和整理的压力，让大脑可以更清楚、更安心地思考。

## 它有什么不同

### 足够简单：先接住一条记录

你不需要先设计一套庞大的分类体系。系统会从 `Raw / Wiki / Outputs` 三层最小结构开始：原始内容先被保留，确认后的理解再进入知识层，需要交付时才生成面向具体受众的输出。

### 足够连接：把点状知识慢慢连成网

一条笔记不会为了“显得丰富”而堆很多链接。它只连接真正有关的来源、主题、依赖和实际应用。时间久了，这些小记录会形成一部属于你的“知识词典”：你不仅能找到某个知识点，也能看到自己曾经怎样理解和使用它。

### 足够个性化：知识库应该适应人

每个人保存的信息、思考方式、隐私边界和维护精力都不同。系统会先了解你的目标、使用场景和现有习惯，再生成最小可用架构。它不会预设你必须拥有怎样的人生分类，也不会要求你把已有知识库推倒重来。

### 足够有成长性：记录“会了什么”，也记录“还缺什么”

书、课程和文章只是输入。真正的成长还需要解释、实践、处理异常和迁移到新场景。系统会把兴趣先放进候选区，不让一个新念头立刻打乱已有计划；也会用真实表现记录能力变化，而不是因为“看完了”或“做成过一次”就判定已经掌握。

### 足够丰富：能陪伴一件事从想法走到完成

它可以记录一个工作或科研项目，也可以记录一段时间的学习与生活。完整过程是：

```text
捕捉 → 保真 → 辨析 → 连接 → 规划 → 实践 → 验证 → 复盘 → 沉淀 → 输出 → 更新
```

你可以保留最初的资料和想法，区分事实与推测，形成计划，在行动中收集证据，复盘判断，再把真正稳定的理解沉淀下来。过程没有走完也没有关系：尚未想清楚、暂时没来得及实践的想法，可以先安全地停在候选区。

### 辅助自我洞察：看见变化，但不急着定义自己

生活中细小的 Inspire Time、反复出现的选择、一次项目中的犹豫或突破，都可能帮助你更了解自己。系统会保留具体情境、你的原话、暂时的解释、其他可能性和反例。它不会根据一件事给你贴上固定标签，也不会进行人格或心理诊断。

## 什么时候调用哪个 Skill

你可以从总入口 `$knowledge-vault` 开始，也可以直接调用下面的子 Skill。

- 如果你还没有知识库，或者现有目录越来越难用，希望先聊清楚需求再建立一个最小架构——调用 `$vault-bootstrap`。
- 如果你想收集日常的点状知识，把小记录积累成“你的知识词典”——调用 `$atomic-notes`。
- 如果你拿到了一篇文章、一段对话、一份会议记录或一批混杂资料，希望保留来源并分清事实、判断和推测——调用 `$knowledge-intake`。
- 如果你希望使用 Obsidian 的 Properties、双链、Backlinks、Bases 或 Dashboard，同时保持普通 Markdown 也能阅读——调用 `$obsidian-vault`。
- 如果你产生了一个学习、技能或项目想法，还没想清楚要不要投入，希望先比较价值、成本与掌握证据——调用 `$growth-system`。
- 如果生活或工作中出现了一个小小的触动，并且它可能改变你以后处理事情的方式——调用 `$inspire-time`。
- 如果你希望记录一个项目从目标、决策、执行到验证的全过程，或在中断后准确接续——调用 `$project-lifecycle`。
- 如果一个项目、一周、一个月或某段经历告一段落，希望根据真实事件理解发生了什么、下一次怎样做得更好——调用 `$retrospective`。
- 如果你想理解自己反复出现的工作方式、偏好、价值取向或判断模式，同时保留反例和修正空间——调用 `$self-observation`。
- 如果你需要把知识库中的内容整理成报告、文章、申请材料或团队简报，并控制受众、来源和披露范围——调用 `$knowledge-output`。
- 如果你的需求跨越多个阶段，或者你还不知道该选哪一个——调用 `$knowledge-vault`，它会帮你找到最短、最合适的路径。

## 它可以记录什么

它适用于工作、科研、学习和生活中需要长期理解与接续的事情，例如：

- 一个项目从问题提出、资料收集、方案比较、执行、验证到交付和复盘的全过程；
- 一项研究从问题、证据、假设、实验、失败记录到阶段结论的形成过程；
- 一门课程或一个技能从输入、解释、练习到真正能够独立应用的过程；
- 一段时间内的计划、推进、事件记录和周期复盘；
- 日常出现的一个 Inspire Time，以及它后来有没有成为现实中的行动；
- 想到了但还没想清楚，或暂时没有精力实践的候选想法；
- 个人目标、偏好和工作方式怎样随着证据逐渐变化；
- 面向不同受众的文章、汇报、申请、总结或公开表达。

这套系统不要求你把生活变成一张巨大的表格。你可以只安装此刻需要的 Skill，也可以让它逐渐长成更完整的个人系统。

## 方法依据

这些理论和著作提供了设计参考。它们支持某一部分方法选择，不代表整套 Skill 已经经过整体效果实验。

| Skill | 方法依据 | 在本系统中的转译 |
|---|---|---|
| `knowledge-vault` | Tiago Forte 的 [Building a Second Brain](https://www.simonandschuster.com/books/Building-a-Second-Brain/Tiago-Forte/9781982167387) | 让信息从收集走向组织、理解和表达；本系统进一步加入证据、成长与自我观察边界 |
| `vault-bootstrap` | [ISO 9241-210 人本设计](https://www.iso.org/standard/77520.html) | 先理解用户、任务和环境，再建立适合这个人的最小结构 |
| `knowledge-intake` | [W3C PROV 信息溯源模型](https://www.w3.org/TR/prov-overview/) | 保留信息的来源、形成过程和责任归属，帮助判断可信度 |
| `atomic-notes` | Sönke Ahrens 的 [How to Take Smart Notes](https://www.soenkeahrens.de/en/takesmartnotes) | 用可独立理解的笔记和有意义的连接支持长期思考与写作 |
| `obsidian-vault` | Vannevar Bush 的 [As We May Think](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/) | 通过关联路径连接信息；Obsidian 只是当前实现载体，不是方法本身 |
| `growth-system` | Ericsson 等人的[刻意练习研究](https://doi.org/10.1037/0033-295X.100.3.363)与《[Make It Stick](https://www.retrievalpractice.org/make-it-stick)》 | 用练习、反馈、提取和迁移证据判断成长，而不是只记录输入 |
| `inspire-time` | David Kolb 的[体验式学习理论](https://www.pearson.com/en-us/subject-catalog/p/Kolb-Experiential-Learning-Experience-as-the-%2520Source-of-Learning-and-Development-2nd-Edition/P200000000384) | 让一次经历经过反思、形成理解，再回到具体实践中验证 |
| `project-lifecycle` | PMI 的[项目过程组](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmief/skills-for-life-english.pdf) | 用启动、规划、执行、监控和收尾保持项目可接续、可验证 |
| `retrospective` | Donald Schön 的 [The Reflective Practitioner](https://www.hachettebookgroup.com/titles/donald-a-schon/the-reflective-practitioner/9780465068784/) | 将行动中的隐性判断带回反思，形成下一次可测试的改变 |
| `self-observation` | Grant、Franklin 与 Langford 的[自我反思与洞察研究](https://doi.org/10.2224/sbp.2002.30.8.821) | 区分“反复想自己”和“形成更清晰的理解”，保留证据、替代解释与反例 |
| `knowledge-output` | Barbara Minto 的 [The Pyramid Principle](https://www.pearson.com/en-gb/subject-catalog/p/the-pyramid-principle/P200000015259/9781292763255) | 先明确受众与结论，再组织支持信息，同时保留来源和披露边界 |

更完整的对应关系和适用边界见 [理论与方法依据](docs/00-overview/theoretical-foundations.md)。

## 这个项目从哪里来

这套 Skill 的最初灵感来自北辰青年宋超老师。

我跟随宋超老师课程中的文档，搭建了自己的基础知识库。真正使用以后，我又慢慢加入了对我很重要的部分：原始证据与稳定理解的分层、成长候选、能力证据、项目全过程、Inspire Time、复盘，以及有证据又允许被修正的自我观察。

感谢北辰青年宋超老师提供了最初的启发和框架。这个仓库是在那份启发之上，结合长期实际使用重新整理出的开源 Skill Suite。希望它也能成为其他人开始整理自己知识与生活的一块踏板。

## 快速开始

1. 克隆仓库，或下载源码。
2. 将需要的目录从 `skills/` 复制到 Codex skills 目录；也可以先运行安装预览：

   ```powershell
   python -X utf8 scripts/install_codex_skills.py <codex-skills-directory> --dry-run
   python -X utf8 scripts/install_codex_skills.py <codex-skills-directory>
   ```

3. 重新打开一个 Codex 任务，让技能被发现。
4. 调用 `$knowledge-vault`，说出你此刻想建立、整理、记录或梳理清楚的事情。
5. 首次建库时，Skill 会先访谈并展示写入预览，获得授权后才创建文件。

完整流程见 [系统总览](docs/00-overview/system-overview.md) 和 [用户旅程](docs/00-overview/user-journey.md)。

## 我们坚持的边界

- 不把 AI 推测写成事实。
- 不因一次成功判定稳定能力。
- 不把输出稿反向当作事实来源。
- 不要求第三方 Obsidian 插件。
- 不把候选想法自动升级成正式任务。
- 不根据一次事件固定地定义一个人。
- 未获得写入授权时，只提供提案和预览。
- 示例全部为虚构内容。

## 验证

```powershell
python -X utf8 scripts/validate_skill_structure.py
python -X utf8 scripts/validate_internal_links.py
python -X utf8 scripts/privacy_scan.py
```

详见 [验证与发布](docs/08-maintainers/validation-and-release.md)。项目采用 [MIT License](LICENSE)。
