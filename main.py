import sys
from stats import get_num_words, get_char_count, sorted_char_count

def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def usage():
    print("Usage: python3 main.py <path_to_book>")

def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    book_path = sys.argv[1]
    text =  get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_count(text)
    sorted_chars = sorted_char_count(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char_count in sorted_chars:
        char = char_count['char']
        num = char_count['num']
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print("============= END ===============")

if __name__ == "__main__":
    main()