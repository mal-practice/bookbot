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

def order_dict(letters):
    return letters["num"]

def sort_dict(letters):
    sort_list = []
    for letter in letters:
        count = letters[letter]
        sort_list.append({"char": letter, "num": count})
    sort_list.sort(reverse=True, key=order_dict)
    return sort_list


