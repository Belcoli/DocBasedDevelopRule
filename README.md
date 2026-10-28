# 文档先行开发 · Document First Development

一个提供开发 guideline、流程与方法论的 Codex 插件。一个技能入口，按任务加载规则、流程和模板；支持新项目接入、已有文档体系映射、契约驱动开发、变更、审核与交接。

**主契约是项目一切有效设计的唯一权威说明。** 可按实际职责维护一份或多份，明确覆盖范围，尽量避免重复描述，彼此不得冲突；每条设计只在一处定义。 Progress 只记录执行与验证，Issues 只记录未决问题与门禁；它们不得定义、复述或覆盖设计。

## 安装

源码仓库：[Belcoli/DocBasedDevelopRule](https://github.com/Belcoli/DocBasedDevelopRule)。使用支持插件命令的 Codex：

```text
codex plugin marketplace add Belcoli/DocBasedDevelopRule
codex plugin add document-first-development@document-first-development-marketplace
```

安装后新开聊天。已有同名本地来源时，先按 [安装说明](docs/install.md) 确认来源，避免混用。

## 使用方式

1. 按 [安装说明](docs/install.md) 添加插件来源并安装。
2. 在目标项目中明确调用 `$document-first-development:document-first-development`，请求接入或处理一个具体任务。
3. 接入时确认项目根、文档根和现有文档职责映射，再在项目已有 AI 指引中登记采用声明与文档入口。
4. 接入后，相关任务按本流程处理；普通小任务复用已有契约，不强制重新立项。

主契约只维护设计，不定义验收要求；非目标仅在开发者明确提出或明确批准/赞同建议时记录。验收在主契约之外按项目既有方式或本次明确沟通约定，实际结果归 Progress。

设计提案、历史/决策记录、调查/审核/证据附件均为可选材料，不要求项目另行建立这些文档。

安装不自动接入所有项目。自动使用依赖客户端读取项目采用声明；插件提供行为指引，不提供文件系统级强制控制。

## 内容入口

- [技能入口](plugins/document-first-development/skills/document-first-development/SKILL.md)
- [核心规则](plugins/document-first-development/skills/document-first-development/references/rules.md)
- [文档职责与维护](plugins/document-first-development/skills/document-first-development/references/documents.md)
- [模板目录](plugins/document-first-development/skills/document-first-development/assets/templates/README.md)
- [安装与跨主机迁移](docs/install.md)
- [维护与分发](docs/maintenance.md)
- [插件设计基线](docs/design.md)

## 支持边界

目标客户端为 Codex 桌面端与 CLI，共用一个插件包；IDE 扩展不纳入本期支持。包结构检查不等于客户端验收。

使用流程不要求 MCP、专属 API、特定 shell、其他技能或联网服务。仓库检查脚本仅供维护者使用，不是技能运行依赖。

插件仓库只维护通用规则、流程、空白模板及安装维护说明。具体项目的主契约、进度、Issue、决策、路径与日志由项目自行维护，不回写插件。

## 许可证

采用 [MIT License](LICENSE)。插件安装包内也保留相同许可证。
