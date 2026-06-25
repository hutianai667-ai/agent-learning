# Stage 1 - LLM Basics

## 1. LLM

LLM 是大语言模型，会根据输入的 prompt 和上下文生成回答。

## 2. Prompt

Prompt 是给大模型的输入。

一个更稳定的 prompt 通常包含：

- 角色
- 任务
- 背景
- 限制
- 输出格式
- 示例

## 3. Token

Token 是大模型处理文本的基本单位，不完全等于人类平时说的字数。

- 中文通常接近一个汉字一个 token
- 英文单词可能是一个 token，也可能被拆成多个 token
- 标点、空格、代码符号也可能算 token

Token 会影响：

- context window
- API cost
- 模型处理速度
- 长文本任务效果

## 4. Context Window

Context window 是模型一次能看见和处理的最大上下文范围。

它的容量通常用 token 计算。

使用 AI Agent 时，不应该一开始让它读取整个项目，而应该：

1. 先看目录结构
2. 再搜索和任务相关的关键词
3. 只读取相关文件
4. 明确禁止读取 `.env`、API key、密码文件
5. 改文件前先说明计划

## 5. Temperature

Temperature 控制模型回答的随机程度。

低 temperature：

- 更稳定
- 更保守
- 适合代码、排错、总结、严格执行

高 temperature：

- 更发散
- 更有创意
- 适合头脑风暴、起名字、文案改写

CLI Agent 多数时候执行真实文件操作，所以更适合低 temperature。

## 6. Cost

Cost 是模型调用成本，通常和输入 token、输出 token、模型类型、调用次数有关。

长 prompt、长文件、多轮对话都会增加 token，从而增加成本。

## 7. 今天的理解

今天通过对比弱 prompt 和结构化 prompt，发现给模型明确的角色、背景、限制和输出格式，会让回答更贴合任务。

今天也理解了 context window 和 token 的关系：

- token 是模型处理文字的小单位
- context window 是一次能容纳多少 token 的范围