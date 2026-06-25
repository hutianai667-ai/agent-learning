import json
import urllib.request

profile_path = "week-01/data/stage0-profile.json"
output_path = "week-01/outputs/stage0-final-check.json"
url = "https://api.github.com/users/torvalds"

with open(profile_path, "r", encoding="utf-8") as file:
    profile = json.load(file)

with urllib.request.urlopen(url) as response:
    github_user = json.load(response)

result = {
    "stage": "Stage 0",
    "local_profile_name": profile["name"],
    "local_skills": profile["skills"],
    "api_user_login": github_user["login"],
    "api_user_name": github_user["name"],
    "api_user_followers": github_user["followers"],
    "safety_check": "No .env or API key was used."
}

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=2)

print(f"Saved Stage 0 final check to {output_path}")