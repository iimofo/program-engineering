from task5_1 import calculate_herons_area

def run_area_app():
    print("--- Modular Triangle Area (Heron's Formula) ---")
    try:
        side_a = float(input("Enter length of side A: "))
        side_b = float(input("Enter length of side B: "))
        side_c = float(input("Enter length of side C: "))
        area = calculate_herons_area(side_a, side_b, side_c)
        if area is not None:
            print(f"\nThe semi-perimeter (s) is: {(side_a + side_b + side_c) / 2}")
            print(f"The calculated area of the triangle is: {area:.2f}")
        else:
            print("\nError: The entered side lengths do not form a valid triangle (Triangle Inequality Theorem).")
    except ValueError:
        print("\nInvalid input. Please enter numerical values for all side lengths.")

if __name__ == '__main__':
    run_area_app()
