from stats import get_num_words
from stats import get_char_count

def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def main():
    text =  get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    char_counts = get_char_count(text)
    print(f"Found {num_words} total words")
    print(char_counts)

if __name__ == "__main__":
    main()