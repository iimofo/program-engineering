def calculate_average_of_args(*args):
    print(f"\n--- Average of Unknown Arguments ---")
    
    num_arguments = len(args)
    
    if num_arguments == 0:
        print("No arguments provided. Average is 0.")
        return 0
    total_sum = sum(args)
    average = total_sum / num_arguments
    print(f"Arguments: {args}")
    print(f"Sum: {total_sum}, Count: {num_arguments}")
    return average

if __name__ == '__main__':
    avg1 = calculate_average_of_args(10, 20, 30, 40, 50)
    print(f"Average 1: {avg1:.2f}")
    avg2 = calculate_average_of_args(1, 2, 6)
    print(f"Average 2: {avg2:.2f}")
    avg3 = calculate_average_of_args()