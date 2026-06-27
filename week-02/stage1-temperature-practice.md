# Stage 1 - Temperature Practice

## 1. Temperature 是什么

Temperature 是控制模型输出随机程度的参数。

- 低 temperature：更稳定、更保守，适合代码、排错、总结、严格执行
- 高 temperature：更发散、更有创意，适合头脑风暴、起名字、文案改写

Temperature 低不代表一定正确，temperature 高也不代表更聪明。它只是控制随机性。

## 2. 任务判断练习

### A. 让 Agent 修改 Python bug

判断：低 temperature

原因：修改 bug 需要稳定、准确，不能随意发散。

### B. 让模型想 20 个 AI 学习计划名字

判断：高 temperature

原因：起名字需要更多创意和多样性。

### C. 让模型总结一份错误日志

判断：低 temperature

原因：总结错误日志需要稳定、准确地提取重点。

### D. 让模型写 5 种广告文案风格

判断：高 temperature

原因：广告文案需要创意和不同风格。

### E. 让 Agent 按步骤修改 GitHub 仓库文件

判断：低 temperature

原因：修改仓库文件属于真实执行任务，需要稳定和可控。

## 3. 稳定版 Prompt

```text
你是一个正在教编程小白的 AI Agent 学习导师。

请解释 context window 是什么。

背景：
我正在学习 Stage 1：LLM 基础，已经了解 token 的概念。

要求：
1. 用中文解释。
2. 不要发散，不要介绍无关概念。
3. 说明 context window 和 token 的关系。
4. 输出不超过 200 字。
5. 不读取 `.env`、API key、密码文件。

输出格式：
定义：
解释：
类比：
注意事项：适合：低 temperature
原因：目标明确、限制清楚、格式固定，需要稳定输出。


4. 创意版 Prompt
你是一个擅长用类比教学的 AI Agent 学习导师。

请用更生动的方式解释 context window。

背景：
我刚开始学习 LLM，希望通过多个类比建立直觉。

要求：
1. 用中文解释。
2. 给 3 个类比：生活类比、电脑类比、Git/Python 类比。
3. 每个类比不超过 80 字。
4. 最后用 3 条 bullet 总结重点。
5. 不读取 `.env`、API key、密码文件。

输出格式：
一句话定义：
生活类比：
电脑类比：
Git/Python 类比：
重点总结：
适合：高 temperature
原因：需要更生动的表达、多个类比和多角度解释，适合适当发散。
5. 我的理解
CLI Agent 操作真实文件、运行命令、修改代码时，应该偏向低 temperature。
创意类任务，比如起名字、写文案、想多个方案，可以使用更高 temperature。
Temperature 不是正确性的保证。真正影响输出质量的还有 prompt 是否清楚、上下文是否相关、是否有验证步骤。