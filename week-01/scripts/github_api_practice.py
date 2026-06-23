import json
import urllib.request

url = "https://api.github.com/users/torvalds"
output_path = "week-01/outputs/github-user-torvalds.json"

with urllib.request.urlopen(url) as response:
    data = json.load(response)

result = {
    "login": data["login"],
    "name": data["name"],
    "followers": data["followers"],
    "public_repos": data["public_repos"],
    "html_url": data["html_url"]
}

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=2)

print(f"Saved GitHub user data to {output_path}")