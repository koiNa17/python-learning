def years_to_100(name, age):
    years_left = 100 - age
    message = f"{name}さんは、あと{years_left}年で100歳です。"
    return message

user_name = input("お名前を入力してください： ")
user_age = int(input("年齢を入力してください： "))

result = years_to_100(user_name, user_age)
print(result)