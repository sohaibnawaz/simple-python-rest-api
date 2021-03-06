import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Grape!", "views": 1000000, "likes": 9383942},
    {"name": "Falling", "views": 3456, "likes": 145},
    {"name": "Crazy Jump", "views": 1343, "likes": 12323}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/6")
print(response.json())

input()
response = requests.patch(BASE + "video/2", {"views":50})
print(response.json())
