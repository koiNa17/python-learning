import csv

# ---------- 道具（ツール箱） ----------
def load_csv(filename):
    """CSVファイルを読み込んで、辞書のリストとして返す"""
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_over30(rows):
    """age が 30 以上の行だけを取り出す"""
    result = []
    for row in rows:
        age = int(row["age"])
        if age >= 30:
            result.append(row)
    return result

def save_csv(filename, rows, fieldnames):
    """辞書のリスト rows を CSV に書き出す"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def add_age_group(rows):
    result = []
    for row in rows:
        age = int(row["age"])

        if 30 <= age < 40:
            group = "30代"
        elif 40 <= age < 50:
            group = "40代"
        else:
            group = "50代〜"

        new_row = row.copy()
        new_row["age_group"] = group
        result.append(new_row)

    return result

# ---------- メイン（ストーリー部分） ----------
def main():
    # ① people.csv を読む
    data = load_csv("people.csv")

    # ② 30歳以上だけに絞る
    over30 = filter_over30(data)

    # ★ 年代列を追加
    over30_with_group = add_age_group(over30)

    print(over30_with_group)

    # ③ over30.csv に書き出す
     # ★ 保存（列を追加したので fieldnames も増やす）
    save_csv(
        "over30.csv",
        over30_with_group,
        fieldnames=["name", "age", "age_group"],
    )


if __name__ == "__main__":
    main()
