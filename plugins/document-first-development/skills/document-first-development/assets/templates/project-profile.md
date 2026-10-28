# {{PROJECT_NAME}} 流程适配

本文只记录项目工作方式和定位策略。功能设计与组件职责写入主契约；验收要求按项目既有方式另行约定，不写入主契约。本文不改变插件核心权威与授权边界。

## 接入

- 文档入口：{{DOC_INDEX_LINK}}
- 采用版本：{{PLUGIN_VERSION}}
- 接入确认来源与范围：{{CONFIRMATION_REFERENCE}}
- 本次适配覆盖：{{PROJECT_OR_SUBPROJECT_SCOPE}}

文档角色映射只在文档入口维护。

## 工作方式

- 需求与设计确认责任：{{RESPONSIBILITY_POLICY}}
- 开发、人工观察、用户验收与 QA 分工：{{VERIFICATION_RESPONSIBILITY_POLICY}}
- Issue 编号与分级名称：{{ISSUE_NAMING_POLICY}}
- 历史、已解决问题和证据保留：{{RETENTION_POLICY}}
- 临时诊断与持久诊断的管理和清理方式：{{DIAGNOSTIC_POLICY}}
- 现有编译/测试/运行入口：{{EXISTING_VERIFICATION_ENTRY_LINKS}}

可以映射项目已有术语，但不得改变 P0/P1/P2/P3 的门禁语义。被验证的设计引用主契约，验收要求遵循项目在主契约之外的约定；这里只约定如何组织验证工作。

## 本地定位

- 项目根定位方式：{{PROJECT_ROOT_LOCATOR}}
- 文档根定位方式：{{DOC_ROOT_LOCATOR}}
- 插件安装定位方式：{{CLIENT_INSTALL_LOCATOR}}

优先使用相对路径或可重新绑定的定位说明；绝对主机路径只留在项目自己的本地信息中。换主机重新确认这三个位置，不改插件核心。

## 更新方式

项目文档自行维护。插件升级先检查流程差异，不自动重写契约、Progress 或 Issues；项目实例不回写插件仓库和安装缓存。
