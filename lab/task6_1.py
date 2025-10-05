def calculate_average(data_list):
    if not data_list:
        return 0
    return sum(data_list) / float(len(data_list))

def process_and_report_kwargs(**kwargs):
    print("--- Processing Keyword Arguments ---")
    for key, value in kwargs.items():
        mean = calculate_average(value)
        print(f"{key}: Mean = {mean}")

if __name__ == '__main__':
    process_and_report_kwargs(
        x=[1, 2, 3],
        y=[3, 3, 0],
        z=[10, 20, 30, 40],
        q=[5]
    )