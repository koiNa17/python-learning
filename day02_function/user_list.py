users = [
    {"name": "Yoshi", "age": 18},
    {"name": "Mika", "age": 25},
    {"name": "Ken", "age": 30},
]

for user in users:
    print(f"{user['name']}さんは{user['age']}歳です")

for user in users:
    if user["age"] >= 30:
        print(f"{user['name']}さんはベテランです！")