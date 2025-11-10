def validate_input(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("数値を入力してください。")
    if b == 0:
        raise ZeroDivisionError("0では割り算できません。")
    return a, b

def safe_divide(a, b):
    try:
        a, b = validate_input(a, b)
        return a / b
    except (TypeError, ZeroDivisionError) as e:
        print(f"⚠️ 入力エラー: {e}")
        return None

if __name__ == "__main__":
    print("10 ÷ 2 =", safe_divide(10, 2))
    print("10 ÷ 0 =", safe_divide(10, 0))
