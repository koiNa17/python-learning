def get_user_info():
    name = "Yoshi"
    age = 35
    city = "Tokyo"
    return name, age, city

info = get_user_info()
print(info)

n, a, c = get_user_info()
print(f"Name: {n}, Age: {a}, City: {c}")