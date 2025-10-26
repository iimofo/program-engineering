import re

def censor_sentence(sentence_to_censor, forbidden_words_file='input.txt'):
    try:
        with open(forbidden_words_file, 'r', encoding='utf-8') as f:
            forbidden_words = f.read().strip().split()
    except FileNotFoundError:
        return f"Error: Forbidden words file '{forbidden_words_file}' not found."
    
    if not forbidden_words:
        return sentence_to_censor

    forbidden_words.sort(key=len, reverse=True)

    censored_sentence = sentence_to_censor
    
    for word in forbidden_words:
        stars = '*' * len(word)
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        censored_sentence = pattern.sub(stars, censored_sentence)

    return censored_sentence


sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... awesome!!!!"

result = censor_sentence(sentence)

print(f"Original: {sentence}")
print(f"Censored: {result}")