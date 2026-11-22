import json, urllib.request

url = "https://jsonplaceholder.typicode.com/users/1"
with urllib.request.urlopen(url) as r:
    data = json.load(r)

with open("API/api_response.json", "w") as f:
    json.dump(data, f, indent=2)

print(json.dumps(data, indent=2))
