# {{PROJECT_OR_MODULE_NAME}} Progress

本文是实际执行与验证结果的唯一权威记录。设计只在主契约；未决问题只在 Issues。这里不写接口、行为定义、设计说明、候选或最终解决方案。

## 工作项

| 工作项编号/对象 | 设计依据（契约修订与条款链接） | 实现状态 | 验证记录引用 | 验收记录引用 | 关联 Issue |
|---|---|---|---|---|---|
| {{WORK_ID_AND_OBJECT}} | {{CONTRACT_REVISION_CLAUSE_LINK}} | {{IMPLEMENTATION_STATUS}} | {{EVIDENCE_LINKS}} | {{ACCEPTANCE_RECORD_LINK}} | {{ISSUE_LINKS_OR_NONE}} |

待开始、进行中与已实现可按项目术语表达；不要用“已完成”隐含全部验证通过。关联 Issue 只放编号/链接。

## 执行记录

| 日期 | 工作项 | 实际操作/产物引用 | 结果 |
|---|---|---|---|
| {{DATE}} | {{WORK_ID}} | {{ACTION_OR_ARTIFACT_REFERENCE}} | {{EXECUTION_RESULT}} |

只写做过什么和产物位置；设计解释引用主契约，不在这里复述。

## 验证记录

| 证据编号 | 对象/实现基线 | 契约依据 | 验证方式与环境 | 结果及覆盖边界 | 原始资料/可用性 |
|---|---|---|---|---|---|
| {{EVIDENCE_ID}} | {{OBJECT_AND_IMPLEMENTATION_BASELINE}} | {{CONTRACT_CLAUSE_LINK}} | {{METHOD_AND_ENVIRONMENT}} | {{ACTUAL_RESULT_AND_LIMITS}} | {{EVIDENCE_LOCATION_AND_AVAILABILITY}} |

静态、编译、自动测试、运行日志、人工观察、用户验收分别记录。观察是有基线的事实，不写成设计规则。小任务可以简化栏目，但保留方式、结果和覆盖范围。

## 验收记录

| 日期/确认来源 | 工作项与基线 | 实际接受的对象与范围 | 证据引用 |
|---|---|---|---|
| {{DATE_AND_ACCEPTANCE_SOURCE}} | {{WORK_ID_AND_BASELINE}} | {{ACCEPTED_OBJECT_AND_SCOPE}} | {{EVIDENCE_LINKS}} |

验收依据来自项目在主契约之外的适用约定，按需引用其来源；这里记录实际接受范围，不定义设计或新增验收标准。

保留历史已通过记录。新增变更建立独立记录，注明只重开哪些条款；不能用旧证据证明新版本，也不能无故撤回无关历史验收。
