receipt_codes = [
    8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
    1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
    5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
    5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
    3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506
]

total_receipts = len(receipt_codes)
unique_visitors_count = len(set(receipt_codes))
visitor_counts = {}
for code in receipt_codes:
    visitor_counts[code] = visitor_counts.get(code, 0) + 1

most_frequent_code = max(visitor_counts, key=visitor_counts.get)
max_visits = visitor_counts[most_frequent_code]


print(f"1. Всего выдано чеков (посещений): {total_receipts}")
print(f"2. Сколько разных людей посетило ресторан: {unique_visitors_count}")
print(f"3. Какой работник посетил ресторан больше всех раз:")
print(f"   Код работника: {most_frequent_code} (Количество посещений: {max_visits})")