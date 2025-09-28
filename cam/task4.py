def process_sentence(sentence):
    print(f"\n--- Обработка предложения: '{sentence}' ---")
    
    length = len(sentence)
    print(f"Длина предложения: {length}")
    
    lower_sentence = sentence.lower()
    print(f"В нижнем регистре: '{lower_sentence}'")
    
    vowels = "aeiou"
    vowel_count = sum(1 for char in lower_sentence if char in vowels)
    print(f"Количество гласных: {vowel_count}")
    
    replaced_sentence = sentence.replace("ugly", "beauty").replace("Ugly", "beauty") 
    print(f"С заменой 'ugly' на 'beauty': '{replaced_sentence}'")
    
    starts_with_the = sentence.startswith("The")
    ends_with_end = sentence.endswith("end")
    
    print(f"Начинается с 'The': {starts_with_the}")
    print(f"Заканчивается на 'end': {ends_with_end}")

process_sentence("The sky is blue and the movie ends tonight.")

process_sentence("This is an ugly picture, but I feel okay.")

process_sentence("Hello, my name is Bob.")