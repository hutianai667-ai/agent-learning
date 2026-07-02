# Stage 2 - Few-shot Classification Practice

## 1. Few-shot 是什么

Few-shot prompt 是给模型少量示例，让模型照着示例完成新任务。

可以这样理解：

- zero-shot：不给示例，直接按任务和规则做
- few-shot：给几个示例，再让模型照着做

## 2. Few-shot 适合什么时候用

Few-shot 适合用于：

- 类别容易混淆
- 规则用文字不容易说清楚
- 输出格式必须稳定
- 已经有几个正确样例
- zero-shot 输出不稳定

## 3. 我的 3 个示例

输入：今天我学习了 token、context window 和 cost。  
输出：LLM

输入：今天我学习了 .gitignore 规则和 .env.example 模板。  
输出：Security

输入：今天我整理了电脑桌面文件夹。  
输出：Other

## 4. 完整 Few-shot Prompt

```text
角色：
你是一个学习记录分类助手。

任务：
我会给你类别列表、分类规则、示例和一条待分类输入。
请根据规则和示例，把待分类输入分到一个最合适的类别中。

类别列表：
只能从以下类别中选择一个：
- Git
- Python
- LLM
- Prompt
- Security
- Other

分类规则：
1. 如果内容涉及 commit、branch、push、pull、fetch、remote、GitHub、.gitignore，选择 Git。
2. 如果内容涉及 Python、json.load、json.dump、文件读写、脚本，选择 Python。
3. 如果内容涉及 token、context window、temperature、cost、模型选择，选择 LLM。
4. 如果内容涉及 prompt、system prompt、zero-shot、few-shot、输出格式，选择 Prompt。
5. 如果内容涉及 .env、API key、密码、隐私文件，选择 Security。
6. 如果同时涉及 Git 忽略规则和密钥安全，优先选择 Security。
7. 如果无法判断，选择 Other。

示例：
输入：今天我学习了 token、context window 和 cost。
输出：LLM

输入：今天我学习了 .gitignore 规则和 .env.example 模板。
输出：Security

输入：今天我整理了电脑桌面文件夹。
输出：Other

待分类输入：
今天我练习了 few-shot prompt 和输出格式。

输出格式：
只输出一个类别名称，不要解释。

限制：
不要读取 `.env`、API key、密码文件或隐私文件。

5. 预期输出
Prompt
6. 我的理解
Few-shot 的重点不是把 prompt 写长，而是给模型正确示例。
好的示例应该包含：
普通分类示例
容易混淆的示例
Other 兜底示例
如果示例本身不准确，模型会学错。