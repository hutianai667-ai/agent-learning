#输入文件路径
input_path = "week-01/inputs/day2-notes.txt"
#输出文件路径
output_path = "week-01/outputs/day2-summary.txt"

#打开输入文件，用读取模式r，as file 表示把打开后的文件对象临时命名未file
#with 会在代码结束后自动关闭文件
#with是关闭窗口，避免长时间占用，open打开输入路径，读 编码规范是utf8，as file 给文件临时赋予一个变量（第一次写得）

with open(input_path, "r", encoding="utf-8" ) as file:
#读取文件内容，保存在content这个变量里面
     content = file.read()
# summary是一个变量，f表示这个一个格式化字符串，没有f的话，len（content会直接显示应为你字母），len是统计content得字符，characters就是一个英文字符的意思，就是一个单词
# Original也是一个英文单词，原始的意思。{conent}是直接把变量里面的原文进行了展示
summary = f"Today I read {len(content)} characters.\n\nOriginal notes:\n{content}"

#with是再代码运行完成后进行文件关闭，输出路径，写的权限，编码utf8,as file表示把打开后的文件临时命名为file
with open(output_path, "w", encoding="utf-8") as file:
#file.write是写到summary里面去，但是不太明白为啥他就不用前面加变量了
    file.write(summary)
#打印f不知道啥意思，结束。保存到输出路径
print(f"Done. Summary saved to {output_path}")
