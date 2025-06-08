def word_count(text):
    words = text.split()
    return len(words)


def characters(text):
    letters = {}
    text = text.lower()
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

    
