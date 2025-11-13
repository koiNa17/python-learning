students = [
    {"name": "Yoshi", "scores": [80, 90, 85]},
    {"name": "Mika", "scores": [75, 88, 92]},
    {"name": "Ken",  "scores": [60, 72, 70]},
]

print(students[0]["scores"][1])

averages = [sum(s["scores"]) / len(s["scores"]) for s in students]
print(averages)