# 验证与发布

1. 对每个 Skill 运行官方快速验证。
2. 运行 `python -X utf8 scripts/run_checks.py`，完成结构、链接、评测清单、Git 历史隐私扫描、安装和最小 Vault 冒烟检查。
3. 对安装、更新或卸载运行 `--dry-run`，核对目标、技能清单和备份位置。
4. 按 [Codex 行为评测](../../tests/evals/README.md) 在全新任务中测试中文触发、相邻边界、授权和输出质量。
5. 分别报告自动契约检查与真实 Agent 评测，不用前者代替后者。
6. 人工检查附件元数据、组合身份风险和对外示例。
7. 更新 `VERSION` 与 `CHANGELOG.md`，再创建版本标签；记录验证环境与限制。

发布范围核对使用 [通用规则映射](source-to-public-rule-map.md) 和 [测试覆盖矩阵](test-coverage-matrix.md)。
