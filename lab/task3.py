
def add_numbers(one, two):
    result = one + two
    return result

if __name__ == '__main__':
    for i in range(5):
        x = 5
        y = 10
        answer = add_numbers(x, y)
        print(f"Loop {i+1}: Result is {answer}")