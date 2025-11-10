import logging

logging.basicConfig(filename="app.log", level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error("ゼロ除算エラー発生", exc_info=True)
        raise

try:
    divide(10, 0)
except ZeroDivisionError:
    print("mainで例外をキャッチ")
