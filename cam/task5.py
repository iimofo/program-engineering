def rank_employees(employee_names_tuple):

    scores_list = []
    
    print("\n--- Enter Performance Scores (1-10) ---")
    for name in employee_names_tuple:
        while True:
            try:
                score = int(input(f"Enter score for {name}: "))
                if 1 <= score <= 10:
                    break
                else:
                    print("Score must be between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        scores_list.append((name, score))

    ranked_list = sorted(scores_list, key=lambda item: item[1], reverse=True)
    
    return ranked_list


employees_1 = ("Alice", "Bob", "Charlie")
print("\n--- Test Case 1 ---")
employees_2 = ("David", "Eve", "Frank")
print("\n--- Test Case 2 ---")
employees_3 = ("Grace",)
print("\n--- Test Case 3 ---")
