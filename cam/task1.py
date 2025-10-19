user_input_str = input("Введите последовательность чисел, разделённых пробелом: ")

data_list = user_input_str.split(' ')

data_tuple = tuple(data_list)

print("Список из начальных данных:", data_list)
print("Кортеж из начальных данных:", data_tuple)
