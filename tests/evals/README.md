# Codex 行为评测

`cases.json` 是可复用的调用评测集，覆盖中文自动触发、相邻 Skill 边界、授权和关键行为。

## 两层验证

1. `validate_eval_cases.py` 自动检查用例格式、Skill 覆盖和边界用例是否齐全。
2. 在全新 Codex 任务中逐条提交 `prompt`，人工记录实际触发的 Skill 和输出行为。

静态检查只能证明评测集完整，不能证明模型行为正确。发布说明必须分别报告：

- `contract validation`：结构、安装、隐私和评测清单检查。
- `agent evaluation`：真实 Codex 调用的通过数、失败用例和所用版本。

## 结果记录格式

```json
{
  "case_id": "zh-route-intake",
  "environment": "Codex desktop",
  "observed_skills": ["knowledge-intake"],
  "assertions_passed": true,
  "notes": "",
  "reviewed_at": "YYYY-MM-DD"
}
```

结果可以保存在 `.test-output/eval-results.jsonl`，不要提交包含真实用户资料的记录。

