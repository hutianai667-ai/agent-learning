import json

input_path = "week-01/data/stage0-profile.json"
output_path = "week-01/outputs/stage0-profile-updated.json"

with open(input_path, "r", encoding="utf-8") as file:
    profile = json.load(file)

profile["skills"].append("JSON")
profile["today_topic"] = "Read and write JSON"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(profile, file, ensure_ascii=False, indent=2)

print(f"Updated JSON saved to {output_path}")