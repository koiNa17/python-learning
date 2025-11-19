import csv
from typing import List, Dict


def load_csv(filename: str) -> List[Dict[str, str]]:
    """CSV を読み込んで「辞書のリスト」として返す（外部境界：大きな try）"""
    rows: List[Dict[str, str]] = []

    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"[ERROR] ファイルが見つかりません: {filename}")
    except OSError as e:
        print(f"[ERROR] ファイルを開けませんでした: {filename} ({e})")
    else:
        print(f"[INFO] 読み込み完了: {filename} rows={len(rows)}")

    return rows


def filter_by_age(rows: List[Dict[str, str]], threshold: int) -> List[Dict[str, object]]:
    """
    年齢でフィルタする。
    - 型変換（str → int）のところだけ、行単位の小さな try を置く
    """
    result: List[Dict[str, object]] = []

    for row in rows:
        raw_age = row.get("age", "").strip()

        try:
            age = int(raw_age)
        except ValueError:
            # raw_age!r で「repr 表示」＝'25 ' みたいに、余計な空白も含めて丸ごと見せる
            print(f"[WARN] 年齢が数値でないのでスキップ: {raw_age!r} row={row}")
            continue

        if age >= threshold:
            new_row = row.copy()
            # ここで age を int にして上書き（以降は「ちゃんと数値」として扱える）
            new_row["age"] = age
            result.append(new_row)

    print(f"[INFO] フィルタ結果: {len(result)} 件 (threshold={threshold})")
    return result


def save_csv(
    filename: str,
    rows: List[Dict[str, object]],
    fieldnames: List[str] | None = None,
) -> None:
    """辞書のリストを CSV に保存する（外部境界：大きな try）"""

    if not rows:
        print("[INFO] 書き出すデータがありません。save_csv をスキップします。")
        return

    # fieldnames が未指定なら、先頭行のキーを使う
    if fieldnames is None:
        fieldnames = list(rows[0].keys())

    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
    except OSError as e:
        print(f"[ERROR] ファイルに書き込めませんでした: {filename} ({e})")
    else:
        print(f"[INFO] 書き込み完了: {filename} rows={len(rows)}")


def main() -> None:
    input_file = "people.csv"
    output_file = "over30_safe.csv"

    # 1) 読み込み（外部境界）
    rows = load_csv(input_file)
    if not rows:
        print("[ERROR] 入力データが空のため終了します。")
        return

    # 2) 年齢フィルタ（行単位の小さな try を内側で使う）
    filtered = filter_by_age(rows, threshold=30)

    # 3) 書き出し（外部境界）
    save_csv(output_file, filtered)


if __name__ == "__main__":
    main()
