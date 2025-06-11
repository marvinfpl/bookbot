from stats import count_words
from stats import count_char
from stats import sort_on
import sys

def get_book_text(file_path: str) ->str:
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit()
    text = get_book_text(sys.argv[1])
    w_count = count_words(text)
    c_count = count_char(text)
    sort = sort_on(c_count)

    print(f"============ BOOKBOT ============\n Analyzing book found at {sys.argv[1]}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {w_count} total words\n")
    print("--------- Character Count -------\n")
    for dic in sort:
        print(f'{dic["char"]}: {dic["num"]}')
    print("============= END ===============")

if __name__ == "__main__":
    main()