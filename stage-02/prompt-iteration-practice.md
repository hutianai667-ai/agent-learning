# Stage 2 - Prompt Iteration Practice

## 1. 今日任务

对同一个学习记录分类 prompt 迭代 5 版，并记录每版差异。

测试输入：

今天我学习了 .gitignore 规则、.env.example 模板和 few-shot prompt。
V1 基础版
问题：
任务和输入容易混在一起
类别不完整
没有分类规则
输出格式不稳定
3. V2 加分类规则
改动：
加入 Git / Python / LLM / Prompt / Security / Other 的分类规则
效果：
分类依据更清楚
但遇到多类别冲突时仍可能摇摆
4. V3 加冲突规则
改动：
加入 Security 优先规则
效果：
.gitignore、.env.example、few-shot prompt 同时出现时，优先选择 Security
5. V4 加 few-shot 示例
改动：
加入普通分类、冲突分类、Other 兜底示例
效果：
模型更容易模仿正确分类方式
6. V5 加检查步骤
改动：
加入检查步骤
输出改成“类别 + 简短理由”
预期输出：
类别：Security
简短理由：同时涉及 .env.example 安全模板和其他类别内容，按 Security 优先规则分类。
7. 今日理解
Prompt 迭代不是一次写出完美版本，而是每次只改一个关键点。
记录每版差异，可以知道 prompt 是因为什么变得更稳定。