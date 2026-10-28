# {{MODULE_NAME}} 主契约

本文件是下述覆盖范围内有效设计的权威说明。项目可维护多份主契约；各份尽量不覆盖相同模块或重复描述同一内容，同一条设计只定义一处，契约之间不得冲突。

- 契约标识：{{CONTRACT_ID}}
- 本契约覆盖范围：{{CONTRACT_SCOPE}}
- 修订标识：{{REVISION}}
- 状态：{{DRAFT_OR_APPROVED_EFFECTIVE}}
- 确认来源、日期与条款范围：{{APPROVAL_REFERENCE_DATE_SCOPE}}
- 需求引用：{{REQUIREMENT_LINKS}}
- 上位/关联契约：{{RELATED_CONTRACT_LINKS}}

待确认稿必须明确标记非生效，不得覆盖既有有效版本。以下栏目按实际模块需要删减；未知设计在对话中讨论，项目需要时才保存非生效提案，不填成确认事实。

## 职责与边界

{{RESPONSIBILITIES_AND_OWNERSHIP}}

明确职责、所有权和协作边界；共用设计引用其权威契约与条款，不复制定义。相关契约变更时核对一致性。

非目标没有默认栏目。仅在开发者明确强调该条目的非目标，或明确批准/赞同建议时，才在适用条目旁简要记录；否则省略，不自行推测或补齐。

## 文件与组件组织

{{FILES_COMPONENTS_AND_RELATIONSHIPS}}

## 接口与行为

每个被记录的接口分别填写以下三组说明；对不适用编程接口的对象，按对应组件入口表达。模块级说明不能替代接口条目，内容可简洁，但不能遗漏适用的逻辑、状态/数据流与生命周期。

### {{CLAUSE_ID}} · {{INTERFACE_OR_BEHAVIOR_NAME}}

#### 名称、签名与调用约定

- 明确名称与完整签名：{{EXACT_NAME_AND_SIGNATURE_OR_COMPONENT_ENTRY}}
- 输入（名称、类型、含义及约束）：{{INPUTS_AND_CONSTRAINTS}}
- 输出（返回值/结果的类型及含义）：{{OUTPUTS_AND_MEANING}}
- 前置条件：{{PRECONDITIONS}}
- 后置条件：{{POSTCONDITIONS}}
- 错误及处理方式：{{ERRORS_AND_HANDLING}}
- 副作用：{{SIDE_EFFECTS}}

无输出或无副作用等情形按实际设计简明注明，不靠留白表达。

#### 内部简要逻辑、状态与数据流

{{BRIEF_MAIN_PATH_KEY_BRANCHES_AND_INTERNAL_CALLS}}

按执行顺序说明读取、处理、分支、状态变化、数据写入及输出；说明关键错误或提前退出对这些步骤的影响。引用共用状态/数据定义，并解释本接口如何使用或改变它们。

{{STATE_AND_DATA_READ_TRANSFORM_WRITE_OUTPUT_RELATIONSHIPS}}

#### 入参及内部变量的生命周期

| 入参/内部变量或同类组 | 来源/创建时点 | 所有者与持有方式 | 使用范围与读写变化 | 结束/释放及调用后存续 |
|---|---|---|---|---|
| {{PARAMETER_OR_INTERNAL_VARIABLE_NAMES_OR_ROLES}} | {{SOURCE_OR_CREATION_POINT}} | {{OWNER_AND_BORROW_COPY_OR_TRANSFER}} | {{USE_SCOPE_AND_MUTATIONS}} | {{LIFETIME_END_CLEANUP_AND_RETENTION}} |

按实际设计说明借用、复制或所有权转移，调用返回后是否仍持有入参或内部对象；涉及异步、回调、缓存或跨调用保留时明确存续边界与释放责任。退出、异常或取消路径有不同清理行为时分别说明。变量作用域、对象存续时间和资源释放责任不得混为一谈。

生命周期相同的变量可分组，但要列明覆盖的名称或角色。尚无实现时用已确认的角色和生命周期描述，不虚构实现变量名。

## 模块级状态与数据流

{{SHARED_STATE_TRANSITIONS_DATA_OWNERSHIP_AND_LIFECYCLE}}

这里只维护跨接口共用的状态和数据定义；各接口引用相关定义，并在自己的条目中说明处理过程与生命周期。

## 不变量与兼容边界

{{INVARIANTS_AND_COMPATIBILITY_RULES}}

## 当前设计的修订索引

必要确认与替代依据可直接在此简短注明；以下表格可裁剪，不要求另建决策或历史文件。

| 修订标识 | 确认来源/日期 | 替代的修订/条款 | 历史依据链接（可选） |
|---|---|---|---|
| {{REVISION}} | {{APPROVAL_REFERENCE_DATE}} | {{SUPERSEDED_REFERENCE}} | {{OPTIONAL_HISTORY_LINK}} |

本文件不定义验收要求、验收标准、验证步骤或证据要求，也不记录任务完成度或未决方案。Progress、Issues 和其他文档不得覆盖、解释或另立本文件的设计。
