from typing import List, Dict


def filter_by_age(rows: List[Dict[str, str]], threshold: int) -> List[Dict[str, object]]:
    result: List[Dict[str, object]] = []

    for row in rows:
        raw_age = row.get("age", "").strip()

        try:
            age = int(raw_age)
        except ValueError:
            print(f"[WARN] 年齢が数値でないのでスキップ: {raw_age!r} row={row}")
            continue

        if age >= threshold:
            new_row = row.copy()
            new_row["age"] = age
            result.append(new_row)

    print(f"[INFO] フィルタ結果: {len(result)} 件 (threshold={threshold})")
    return result
