age = int(input("貴方の年齢を入力してください：　"))

if age < 13:
    print("こども料金です")
elif age < 20:
    print("学生料金")
elif age < 65:
    print("大人料金")
else:
    print("シニア料金")

print("ご利用ありがとう")