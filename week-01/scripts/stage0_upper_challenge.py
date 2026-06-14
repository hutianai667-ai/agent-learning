items = []

items.append(input("First item: "))
items.append(input("Second item: "))
items.append(input("Third item: "))

def build_line(index, item):
    return f"{index},  I learned {item}"

summary = ""

for index, item in enumerate(items, start=1):
    line = build_line(index, item)
    summary = summary + line + "\n"

if len(items) == 3 :
    summary = summary + "Challenge completed.\n"
else :
   summary = summary + "Need more items.\n"


output_path = "week-01/outputs/stage0-upper-challenge.txt"
with  open(output_path, "w", encoding="utf-8") as file:
    file.write(summary)

print(f"Saved challenge result to {output_path}")