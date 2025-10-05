import math

def calculate_herons_area(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return None
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area