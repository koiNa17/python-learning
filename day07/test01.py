print("ファイルを読み込みます…")

try:
    f = open("存在しないファイル.txt")
    content = f.read()
    print(content)

except:
    print("ファイルが見つかりませんでした（優しく受け止めたよ）")

print("→ プログラムは止まらず最後まで進む。")
