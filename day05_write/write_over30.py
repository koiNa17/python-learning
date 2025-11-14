import csv

# Step1: people.csv を読み込む
people = []
with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["age"] = int(row["age"]) # ageを整数にしておく
        people.append(row)

print(people)

# Step2: 30歳以上だけ抽出
over30 = [p for p in people if p["age"] >= 30]

# Step3: over30.csv に書き出す
with open("over30.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames =["name", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(over30)

print("完了！over30.csvを作成しました。")
