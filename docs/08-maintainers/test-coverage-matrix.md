# 测试覆盖矩阵

`自动契约`指脚本可直接判断的结构、安装、链接和隐私规则。`Agent 评测`指必须在真实 Codex 任务中观察的路由与行为。

| Skill | 中文触发 | 相邻边界 | 未授权行为 | 独立安装 | Agent 评测 |
|---|---:|---:|---:|---:|---:|
| knowledge-vault | ✓ | ✓ | ✓ | 随完整套件 | 待运行 |
| vault-bootstrap | ✓ | ✓ | ✓ | ✓ | 待运行 |
| knowledge-intake | ✓ | ✓ | ✓ | ✓ | 待运行 |
| atomic-notes | ✓ | ✓ | ✓ | ✓ | 待运行 |
| obsidian-vault | ✓ | ✓ | ✓ | ✓ | 待运行 |
| growth-system | ✓ | ✓ | ✓ | ✓ | 待运行 |
| inspire-time | ✓ | ✓ | ✓ | ✓ | 待运行 |
| project-lifecycle | ✓ | ✓ | ✓ | ✓ | 待运行 |
| retrospective | ✓ | ✓ | ✓ | ✓ | 待运行 |
| self-observation | ✓ | ✓ | ✓ | ✓ | 待运行 |
| knowledge-output | ✓ | ✓ | ✓ | ✓ | 待运行 |

触发与边界用例见 [Codex 行为评测](../../tests/evals/README.md)。在真实调用结果被记录前，不得把本表中的用例存在误写成行为已经通过。

