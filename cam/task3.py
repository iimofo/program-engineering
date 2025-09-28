try:
    num = int(input("Введите число от 0 до 10: "))
except ValueError:
    print("Ошибка: Введено нечисловое значение.")
    exit()

if not (0 <= num <= 10):
    print("Ошибка: Число должно быть от 0 до 10 включительно.")
    exit()

if 0 <= num <= 3:
    result = "от 0 до 3 включительно"
elif 3 < num <= 6:
    result = "от 3 до 6"
else:
    result = "от 6 до 10 включительно"
    
print(f"Число находится в диапазоне: {result}")