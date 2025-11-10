import logging

# ログ設定
logging.basicConfig(
    filename="app.log",        # 出力先ファイル
    level=logging.ERROR,       # 記録するレベル
    format="%(asctime)s [%(levelname)s] %(message)s"
)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.error(f"エラー発生: {e}")
