def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    from stats import word_count
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    from stats import characters
    letters = characters(text)
    print(letters)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()