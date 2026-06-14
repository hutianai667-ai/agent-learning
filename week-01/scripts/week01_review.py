def build_line(index, item):
    return f"{index}. I practiced {item}"

items = [ ]

items.append("Git status add commit push")
items.append("Python input and print")
items.append("function def return")
items.append("if elif else")
items.append("list and for")

lines = [ ]

for index, item in enumerate(items, start=1):
    line = build_line(index, item)
    lines.append(line)

summary = "Week 01 Review\n\n"

for line in lines:
    summary = summary + line + "\n"

if len(items) >= 5:
    summary = summary + "\nResult: Stage 0 upper practice is getting solid.\n"
else:
    summary = summary + "\nResult: Need more practice.\n"

output_path = "week-01/outputs/week01-review.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(summary)

print(f"Saved review to {output_path}")