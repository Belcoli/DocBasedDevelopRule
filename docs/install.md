# 安装与跨主机迁移

插件名：`document-first-development`。Marketplace 名：`document-first-development-marketplace`。目标是 Codex 桌面端与 CLI 共用同一份包；实际覆盖见 [验证记录](../validation/report.md)。

## 从 GitHub 安装

源码仓库为 [Belcoli/DocBasedDevelopRule](https://github.com/Belcoli/DocBasedDevelopRule)。使用支持插件命令的 Codex：

```text
codex plugin marketplace add Belcoli/DocBasedDevelopRule
codex plugin add document-first-development@document-first-development-marketplace
```

需要固定已发布 Git ref 时，向第一条命令追加 `--ref REF`；REF 应是仓库实际存在的 tag 或提交引用。名称相同但来源不同的 marketplace 不能混用。

本仓库通过 GitHub marketplace 分发；上传源码不等于上架公共插件目录。

此前已登记同名本地来源时，先通过客户端的来源管理确认当前来源，再选择保留本地开发来源或切换到上述 GitHub 来源。不要把两个不同来源作为同一个 marketplace 混用。

## 从本地源码测试

在本仓库根目录执行：

```text
codex plugin marketplace add .
codex plugin add document-first-development@document-first-development-marketplace
codex plugin list --marketplace document-first-development-marketplace --json
```

这些命令会改变执行该命令所用 Codex 配置中的来源和安装状态。需要隔离测试时使用独立的测试配置目录，不更改日常安装。

CLI 命令和选项以本机 `codex plugin --help` 为准；不支持时先确认客户端版本，不手工伪造安装状态。

## 桌面端验证

在桌面端插件页面确认新增来源和插件可见，并完成该版本要求的安装/启用。安装后按客户端提示重启或新开对话。使用 CLI 登记的来源时，先确认桌面端与 CLI 使用同一个配置环境。

在目标项目的新对话中明确调用：

```text
使用 $document-first-development:document-first-development，先识别本项目已有文档体系，
提出职责映射和接入范围；本次先不要修改任何文件。
```

确认技能及相对引用可读取、能够区分主契约/Progress/Issues，且遵守只读请求。随后在用户授权下完成项目接入，使用新对话检验采用声明是否能使相关任务进入流程。

桌面能显示插件、后端能列出技能、模型能按流程执行是不同验证项。CLI 同样需要独立记录加载与行为结果。不要因为共用包而宣布两个客户端都已验收。

## 项目接入

按 [接入指引](../plugins/document-first-development/skills/document-first-development/workflows/onboarding.md) 处理。插件安装位置不是项目文档位置；模板应复制到项目确认的文档根，不能在安装缓存中填写。

## 更新

维护者先更新唯一源中的包版本并验证。使用方通过当前客户端提供的来源更新及插件更新流程升级；可用的来源更新命令为：

```text
codex plugin marketplace upgrade document-first-development-marketplace
```

来源刷新与运行中的会话加载不一定同时发生；升级后核对实际版本并新开会话。不要直接修改安装缓存，也不要由升级自动迁移项目契约或状态文档。

## 跨主机迁移

1. 在新主机通过同一个仓库/ref 安装插件。
2. 重新确认项目根、文档根和客户端安装位置。
3. 修正项目本地定位信息，保留文档职责和条款编号。
4. 检查采用声明到文档入口、契约、Progress 和 Issues 的链接。
5. 核实证据资料的可用性；历史执行结论与当前能否复现分别表达。

项目资料和插件分别迁移；项目实例不进入插件仓库。

## 官方格式依据

- [插件打包、marketplace 与本地客户端配置](https://developers.openai.com/plugins/build/plugins)
- [技能格式与加载](https://developers.openai.com/codex/skills)

本包使用官方仍支持的 `.codex-plugin/plugin.json` 兼容清单。具体客户端兼容性以实测版本和记录为准，不由文件名推断。
