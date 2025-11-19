from data_io import load_csv, save_csv
from filters import filter_by_age


def main() -> None:
    input_file = "people.csv"
    output_file = "over30_safe.csv"

    rows = load_csv(input_file)
    if not rows:
        print("[ERROR] 入力データが空のため終了します。")
        return

    filtered = filter_by_age(rows, threshold=30)

    save_csv(output_file, filtered)


if __name__ == "__main__":
    main()
 