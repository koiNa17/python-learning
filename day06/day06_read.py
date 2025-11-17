import csv

def load_csv(filename):
    rows = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def filter_over30(rows):
    result = []
    for row in rows:
        age = int(row["age"])  # ← ここが最重要！
        if age >= 30:
            result.append(row)
    return result


data = load_csv("people.csv")
print(data)

loaded = load_csv("people.csv")
over30 = filter_over30(loaded)
print(over30)

