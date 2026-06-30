# Stage 2 - Zero-shot Classification Practice

## 1. Zero-shot 是什么

Zero-shot prompt 是不给示例，直接让模型完成任务。

分类任务中，zero-shot prompt 通常需要包含：

- 角色
- 任务
- 类别列表
- 分类规则
- 输入内容
- 输出格式
- 限制

## 2. 分类任务练习

类别列表：

- Git
- Python
- LLM
- Prompt
- Security
- Other

| 输入内容 | 分类 | 原因 |
|---|---|---|
| 今天我学习了 git fetch 和 git pull 的区别。 | Git | fetch 和 pull 都是 Git 操作 |
| 今天我学习了 json.load 和 json.dump。 | Python | 这两个方法用于 Python 处理 JSON |
| 今天我学习了 token、context window 和 cost。 | LLM | 都是 LLM 基础概念 |
| 今天我练习了 system prompt 和输出格式。 | Prompt | 属于提示词设计内容 |
| 今天我学习了 .env 和 API key 为什么不能上传。 | Security | 涉及密钥和安全边界 |
| 今天我整理了电脑桌面文件夹。 | Other | 不属于当前分类体系 |

## 3. 我的初版 Prompt

```text
角色：你是一个具备分类能力的专家

任务：需要帮我进行内容分类，今天我学习了 .gitignore 规则和 .env.example 模板。

类别列表：Git、Python、LLM、Prompt、Security、Other

分类规则：每个学习内容只能对应一个类别列表

输入内容：按照今天学习的内容进行分类

输出格式：用 bullet 进行输出要点，中文输出

限制：不要碰密码文件，.env 文件和 API key 文件

修正版 Zero-shot 分类 Prompt
角色：
你是一个学习记录分类助手。

任务：
请把输入的学习记录分到一个类别中。

类别列表：
只能从以下类别中选择一个：
- Git
- Python
- LLM
- Prompt
- Security
- Other

分类规则：
如果内容涉及 commit、branch、push、pull、fetch、remote、GitHub、.gitignore，选择 Git。
如果内容涉及 Python、json.load、json.dump、文件读写、脚本，选择 Python。
如果内容涉及 token、context window、temperature、cost、模型选择，选择 LLM。
如果内容涉及 prompt、system prompt、zero-shot、few-shot、输出格式，选择 Prompt。
如果内容涉及 .env、API key、密码、隐私文件，选择 Security。
如果同时涉及 Git 忽略规则和密钥安全，优先选择 Security。
如果无法判断，选择 Other。

输入内容：
今天我学习了 .gitignore 规则和 .env.example 模板。

输出格式：
只输出类别名称，不要解释。

限制：
不要读取 `.env`、API key、密码文件。
5. 预期输出
Security
6. 我的理解
Zero-shot 分类 prompt 不给示例，所以类别列表和分类规则必须写清楚。
如果输入内容可能同时属于多个类别，需要增加冲突规则，否则模型可能分类不稳定。
输出格式也要明确限制，比如“只输出类别名称，不要解释”，否则模型可能输出多余内容。