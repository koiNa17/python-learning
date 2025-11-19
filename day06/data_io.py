import csv
from typing import List, Dict


def load_csv(filename: str) -> List[Dict[str, str]]:
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


def save_csv(
    filename: str,
    rows: List[Dict[str, object]],
    fieldnames: List[str] | None = None,
) -> None:
    if not rows:
        print("[INFO] 書き出すデータがありません。save_csv をスキップします。")
        return

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
