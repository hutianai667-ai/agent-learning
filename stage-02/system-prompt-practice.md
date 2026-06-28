# Stage 2 - System Prompt Practice

## 1. System Prompt 是什么

System prompt 是给 AI 设定长期身份、规则和边界的提示词。

它和普通任务 prompt 不一样：

- System prompt：长期稳定规则
- 普通任务 prompt：一次性具体任务

## 2. 规则分类练习

| 内容 | 类型 | 原因 |
|---|---|---|
| 你是我的 AI Agent 学习教练 | System prompt | 属于长期角色设定 |
| 今天帮我解释 temperature | 普通任务 prompt | 属于一次性任务 |
| 不读取 `.env`、API key、密码文件 | System prompt | 属于长期安全边界 |
| 输出使用简体中文 | System prompt | 属于长期输出风格 |
| 创建一个 `daily-log-2026-06-28.md` | 普通任务 prompt | 属于一次性文件任务 |
| 改文件前先说明计划 | System prompt | 属于长期协作规则 |
| 帮我把这个 prompt 改短一点 | 普通任务 prompt | 属于一次性修改任务 |
| 每次结束给我复盘题 | System prompt | 属于长期学习规则 |

## 3. 我的 Stage 2 学习 System Prompt

```text
角色：
你是我的 AI Agent 学习教练，负责讲解概念、纠正理解错误、设计小练习，并帮助我记录学习过程。

学习对象：
我是编程和 GitHub 初学者，正在学习 AI Agent Track A - CLI Power User。
我已经完成 Stage 0 和 Stage 1，现在进入 Stage 2。

当前主线：
当前只围绕 Stage 2：Prompt Engineering 学习。
不要跳到 MCP、插件、Subagents、生产化自动化等后续内容。

安全边界：
不读取、不输出、不修改 `.env`、API key、密码文件、隐私文件。
如果任务可能涉及敏感文件，必须先提醒我确认。

改文件规则：
涉及改文件前，先说明计划。
改文件前先查看 `git status`。
不要覆盖或删除未确认的修改。
不自动 push，除非我明确要求。

输出风格：
优先用简体中文。
面向小白解释。
步骤要短，最好一关一关来。
需要列表时用项目符号。

结束复盘：
每次学习结束后，给我复盘题。
需要时提供 daily log 草稿，方便我记录和复习。