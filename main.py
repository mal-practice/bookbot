from stats import word_count, characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    letters = characters(text)
    print(letters)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()