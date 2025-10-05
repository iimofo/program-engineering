def analyze_and_calculate(x, *args):
    one = x * 10 
    two = sum(args)  
    three = float(len(args)) 
    print(f"one={one} | two={two} | three={three}") 
    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = analyze_and_calculate(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nFinal result={result}")