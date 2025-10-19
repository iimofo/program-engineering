
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
bob = ("Георгий", 41, "Yandex")

personal_info(*tom)

personal_info(*bob)
