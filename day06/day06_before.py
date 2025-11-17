def save_csv(filename, data, fieldnames):
    import csv
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

print(save_csv)

def main():
    people = [
        {"name": "Yoshi", "age": 47},
        {"name": "Mika", "age": 25},
        {"name": "Ken",  "age": 30},
        {"name": "Aki",  "age": 19},
    ]

    over30 = [p for p in people if p["age"] >= 30]
    save_csv("over30.csv", over30, ["name", "age"])

    print("完成（After版）")


if __name__ == "__main__":
    main()
