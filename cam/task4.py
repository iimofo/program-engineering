list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list_2 = [4, 2, 3, 5, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list_3 = [5, 4, 3, 3, 4, 3, 5, 5, 5, 3, 3, 4, 4]

def clean_grades(grades):
    grades_threes_fixed = [4 if grade == 3 else grade for grade in grades]
    final_grades = [grade for grade in grades_threes_fixed if grade != 2]
    
    return final_grades

result_1 = clean_grades(list_1)
result_2 = clean_grades(list_2)
result_3 = clean_grades(list_3)


print(f"Исходный список 1: {list_1}")
print(f"Обновленный список 1: {result_1}")
print("-" * 30)
print(f"Исходный список 2: {list_2}")
print(f"Обновленный список 2: {result_2}")
print("-" * 30)
print(f"Исходный список 3: {list_3}")
print(f"Обновленный список 3: {result_3}")