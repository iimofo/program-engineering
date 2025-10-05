result = None 

def calculate_rectangle_area():
    try:
        width = float(input("Enter Width: "))
        height = float(input("Enter Height: "))
        global result 
        result = width * height
    except ValueError:
        print("Invalid input for rectangle dimensions. Please enter numbers.")

def calculate_triangle_area():
    try:
        base = float(input("Enter Base: "))
        height = float(input("Enter Height: "))
        global result
        result = 0.5 * base * height
    except ValueError:
        print("Invalid input for triangle dimensions. Please enter numbers.")

if __name__ == '__main__':    
    figure = input("Choose figure (1-Rectangle, 2-Triangle): ")
    if figure == '1':
        calculate_rectangle_area()
    elif figure == '2':
        calculate_triangle_area()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
    if result is not None:
        print(f"\nCalculated Area: {result}")