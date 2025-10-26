def calculate_highest_average(filename='grades.txt'):
    best_student_name = None
    highest_average = -1.0
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')
                if len(parts) < 2:
                    print(f"Warning: Skipping malformed line: {line}")
                    continue
                
                name = parts[0].strip()
                grade_strings = parts[1:]
                
                try:
                    grades = [float(g.strip()) for g in grade_strings]
                    
                    if grades:
                        current_average = sum(grades) / len(grades)
                        print(f"Student: {name}, Average Grade: {current_average:.2f}")
                        
                        if current_average > highest_average:
                            highest_average = current_average
                            best_student_name = name
                    
                except ValueError:
                    print(f"Warning: Skipping line due to invalid grade format for {name}.")
                    continue
            
    except FileNotFoundError:
        return f"Error: Grade file '{filename}' not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

    print("-" * 40)
    if best_student_name:
        return f"The student with the highest average ({highest_average:.2f}) is: {best_student_name}"
    else:
        return "No valid student data found."

print(calculate_highest_average())