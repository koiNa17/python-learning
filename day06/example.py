def save_pairs(filename, pairs):
    with open(filename, "w", encoding="utf-8") as f:
        for name, age in pairs:
            f.write(f"{name},{age}\n")

people = [
    ("Yoshi", 47),
    ("Mika", 25),
    ("Ken", 30)
]

save_pairs("people.csv", people)
