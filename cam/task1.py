import string
from collections import Counter

def analyze_article(filename='article.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    if not words:
        return "The file is empty or contains no valid words."

    word_counts = Counter(words)
    total_word_count = len(words)

    most_common = word_counts.most_common(1)
    if not most_common:
        return "No frequent word found."

    most_frequent_word, frequency = most_common[0]

    result = (
        f"--- Analysis of {filename} ---\n"
        f"Total words found: {total_word_count}\n"
        f"Most frequent word: '{most_frequent_word}' (Frequency: {frequency})\n"
        f"{'-' * 30}"
    )
    
    print(result)
    return result

analyze_article('article.txt')