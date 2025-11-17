import csv

# ---------- 道具（ツール箱） ----------
def load_csv(filename):
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_over30(rows):
    return [row for row in rows if int(row["age"]) >= 30]

def save_csv(filename, rows, fieldnames):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# ---------- メイン（ストーリー） ----------
data = load_csv("people.csv")
over30 = filter_over30(data)

save_csv(
    "over30.csv",
    over30,
    fieldnames=["name", "age"]
)
