# Stage 1 - Token / Context / Cost Practice

## 1. Token / Cost 风险判断

### 任务 A

Prompt：请用 100 字解释 git status 是什么。

判断：低 token / 低 cost

原因：任务短，输出长度明确，输入和输出都比较少。

### 任务 B

Prompt：请读取整个 agent-learning 仓库，帮我找出所有可以优化的地方，并写一份详细报告。

判断：高 token / 高 cost

原因：读取范围太大，优化目标不明确，输出要求详细报告，会占用大量 context window。

### 任务 C

Prompt：请只查看 week-02 目录下的 Stage 1 笔记，用 5 条 bullet 总结 token、context window、temperature、cost 的区别。

判断：中低 token / 可控 cost

原因：读取范围明确，输出格式明确，只需要 5 条项目符号列表。

## 2. 坏 Prompt 改写

### 原始 Prompt

把整个项目看一下，然后告诉我怎么学 AI Agent。

### 改写后的 Prompt

请只读取 E:\AI学习资料\agent-learning\week-01 目录下的学习笔记和练习文件。

任务目标：
基于 week-01 的内容，判断我 Stage 0 是否还有薄弱点，并给出下一步学习建议。

安全限制：
不要读取 `.env`、API key、密码文件或隐私文件。

输出要求：
用中文输出，按「阅读 / 实操 / 复盘」三个标题组织。
每个标题下控制在 100 字左右。
如果信息不足，请说明需要我补充什么，不要猜测。

## 3. 我的理解

Token 和 cost 不只取决于问题本身，也取决于读取范围、输出长度和任务轮次。

更好的 prompt 应该明确：

- 读取范围
- 安全边界
- 任务目标
- 输出格式
- 输出长度

# Daily Log - 2026-06-26

## 今天阶段

Stage 1 第 2 节：Token / Context / Cost 估算意识

## 今天阅读

今天学习了输入 token、输出 token、context window 和 cost 的关系。

输入 token 包括用户输入、聊天历史、文件内容、工具返回结果等。
输出 token 主要是模型生成的回答、解释、代码、总结和列表。

## 今天实操

今天完成了 token / cost 风险判断练习：

- 任务 A：短问题 + 100 字限制，判断为低 token / 低 cost
- 任务 B：读取整个仓库 + 详细报告，判断为高 token / 高 cost
- 任务 C：只读取 week-02 + 5 条 bullet 输出，判断为中低 token / 可控 cost

今天还把一个坏 prompt 改写成更适合 CLI Agent 的版本，明确了读取范围、安全边界、任务目标、输出格式和输出长度。

## 今天理解

Token 和 cost 不只取决于问题本身，也取决于：

- 读取范围
- 输出长度
- 聊天历史
- 工具返回内容
- 任务轮次

更好的 prompt 应该避免“读取整个项目”这种大范围指令，而应该先限定目录、限定目标、限定输出，并明确不要读取 `.env`、API key、密码文件。

## 今天纠正

`bullet` 是项目符号列表，通常是：

- 第一条
- 第二条
- 第三条

不是必须用 1、2、3 编号。

## 安全边界

今天没有读取、输出、修改 `.env`、API key、密码文件。

## 明天计划

继续 Stage 1，练习 temperature 对比，理解稳定输出和创意输出的区别。