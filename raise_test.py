def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("divide()でゼロ除算を検知しました")
        raise  # ← ここで“再送（再raise）”

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("main()で例外を再キャッチ:", e)
