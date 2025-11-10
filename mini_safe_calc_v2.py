# mini_safe_calc_v2.py
import logging
from logging.handlers import RotatingFileHandler

# ===== 例外設計 =====
class AppError(Exception): ...
class ValidationError(AppError): ...
class CalcError(AppError): ...

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise CalcError("0で割ることはできません") from e

def run(expr: str):
    try:
        a, b = map(float, expr.split("/"))
    except Exception as e:
        raise ValidationError(f"式が不正です: {expr!r}（例: '10/2'）") from e
    return safe_divide(a, b)

# ===== ロギング設計 =====
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

fh = RotatingFileHandler("app.log", maxBytes=200_000, backupCount=5, encoding="utf-8")
fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s %(message)s")
fh.setFormatter(fmt)
logger.addHandler(fh)

def main():
    test_inputs = ["10/2", "10/0", "abc"]
    for expr in test_inputs:
        try:
            result = run(expr)
            logger.info(f"OK: {expr} => {result}")
            print(f"OK: {expr} = {result}")
        except AppError as e:
            logger.warning(f"BUSINESS ERROR: {e}", exc_info=True)
            print(f"[注意] {e}")
        except Exception as e:
            logger.error(f"UNEXPECTED: {e}", exc_info=True)
            print("[致命] 想定外のエラーが発生しました。ログを確認してください。")

if __name__ == "__main__":
    main()
