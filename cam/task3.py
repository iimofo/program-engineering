import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

all_elements = one + two + three

max_side = max(all_elements)
min_side = min(all_elements)

def calculate_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Не является треугольником (нарушено неравенство)"
    s = (a + b + c) / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
area_max_triangle = calculate_area(max_side, max_side, max_side)
area_min_triangle = calculate_area(min_side, min_side, min_side)


print(f"Максимальный элемент: {max_side}")
print(f"Минимальный элемент: {min_side}")
print("-" * 30)

print("Площадь треугольника (стороны = max):")
print(f"Стороны: {max_side}, {max_side}, {max_side}")
print(f"Площадь: {area_max_triangle:.2f}")

print("-" * 30)
print("Площадь треугольника (стороны = min):")
print(f"Стороны: {min_side}, {min_side}, {min_side}")
print(f"Площадь: {area_min_triangle:.2f}")