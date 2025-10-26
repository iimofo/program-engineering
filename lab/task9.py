def longest_words(file):
    max_length = 0
    sought_words = []
    
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        if words:
            max_length = len(max(words, key=len))
            
        for word in words:
            if len(word) == max_length:
                sought_words.append(word)

    if len(sought_words) == 1:
        return sought_words[0]
    return sought_words

print(longest_words('input.txt'))