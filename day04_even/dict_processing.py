import csv

def read_people(filename):
    rows = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def main():
    data = read_people("people.csv")

    total = 0
    count = 0

    for row in data:
        total += int(row["age"])
        count += 1
    
    ave = total / count
    print("平均年齢：", ave)

    nation_count = {}

    for row in data:
        nation = row["country"]

        if nation in nation_count:
            nation_count[nation] += 1
        else:
            nation_count[nation] = 1
    
    print("国別人数：", nation_count)

    filtered = []

    for row in data:
        if int(row["age"]) >= 30:
            filtered.append(row)
    
    print("30歳以上：", filtered)

    # ④ 抽出した結果を CSV に書き出す
    with open("filtered.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["name", "age", "country"]   # CSV の列順
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()     # ← ヘッダー行を書く
        writer.writerows(filtered)  # ← リスト丸ごと書き込む
    print("filtered.csv に書き出しました！")

if __name__ == "__main__":
    main()
