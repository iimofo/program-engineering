run_results = [
    10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 
    35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4
]

sorted_results = sorted(run_results)
three_best = sorted_results[:3]
three_worst = sorted_results[-3:]
results_from_10th = sorted_results[9:]

print("1. Три лучшие результата (самые низкие времена):", three_best)
print("2. Три худшие результата (самые высокие времена):", three_worst)
print("3. Все результаты начиная с 10-го:", results_from_10th)