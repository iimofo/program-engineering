from collections import Counter

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def convert_list_to_special_set(input_list):
    counts = Counter(input_list)
    
    result_set = set()
    
    for number, count in counts.items():
        result_set.add(number)
        num_str = str(number)
        for i in range(1, count + 1):
            result_set.add(num_str * i)
            
    return result_set

set_1 = convert_list_to_special_set(list_1)
set_2 = convert_list_to_special_set(list_2)
set_3 = convert_list_to_special_set(list_3)


print(f"list_1 -> set_1: {set_1}")
print(f"list_2 -> set_2: {set_2}")
print(f"list_3 -> set_3: {set_3}")