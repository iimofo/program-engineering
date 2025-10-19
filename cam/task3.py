from collections import Counter

def top_3_most_frequent_digits(digit_string):
    counts = Counter(digit_string)

    most_common = counts.most_common(3)

    result_dict = {}
    for digit_char, count in most_common:
        digit_int = int(digit_char)
        result_dict[digit_int] = count
    sorted_result_dict = {
        key: value 
        for key, value in sorted(result_dict.items())
    }
    
    return sorted_result_dict

digit_sequence = "012345678901234567890"
test_string = "011222333344444" 

print(top_3_most_frequent_digits(test_string))