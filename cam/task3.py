import string

def calculate_text_stats(filename='input.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

    total_lines = len(lines)
    total_letters = 0
    total_words = 0
    
    full_text = "".join(lines)
    
    for char in full_text:
        if 'a' <= char.lower() <= 'z':
            total_letters += 1
            
    translator = str.maketrans('', '', string.punctuation)
    text_without_punc = full_text.translate(translator).strip()
    words = text_without_punc.split()
    total_words = len(words)

    print(f"Input file contains:")
    print(f"{total_letters} letters")
    print(f"{total_words} words")
    print(f"{total_lines} lines")

calculate_text_stats()