from math import sqrt, sin, cos, radians

def calculate_math_functions():
    try:
        value = float(input("Enter a value (number): "))        
        root = sqrt(value)
        value_in_radians = radians(value)
        sine = sin(value_in_radians)
        cosine = cos(value_in_radians)
        print(f"\nResults for the value {value}:")
        print(f"Square Root: {root:.4f}")
        print(f"Sine (of {value} degrees): {sine:.4f}")
        print(f"Cosine (of {value} degrees): {cosine:.4f}")
        
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    calculate_math_functions()