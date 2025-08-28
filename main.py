import sys

from stats import (
    book_words,
    letter_count,
    chars_sorted_list,
)
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    n = book_words(text)
    c = letter_count(text)
    sorted = chars_sorted_list(c)
    print_report(book_path, n, sorted)

def get_book_text(file_path):
    with open(file_path) as f:
       return f.read()

def print_report(a, b, c):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {a}...")
    print("----------- Word Count ----------")
    print(f"Found {b} total words")
    print("--------- Character Count -------")
    for i in c:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()