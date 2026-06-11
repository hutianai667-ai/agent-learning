input_path = "week-01/inputs/day2-notes.txt"
output_path = "week-01/outputs/day2-summary.txt"

with open(input_path, "r", encoding="utf-8" ) as file:
     content = file.read()

summary = f"Today I read {len(content)} characters.\n\nOriginal notes:\n{content}"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(summary)

print(f"Done. Summary saved to {output_path}")
