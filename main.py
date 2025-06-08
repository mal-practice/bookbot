import sys
from stats import (word_count, characters, sort_dict)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)   
    letter_dict = characters(text)
    result = sort_dict(letter_dict)
    print_report(book_path, num_words, result)
        
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, result):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in result:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()