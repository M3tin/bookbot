from stats import get_num_chars, get_num_words
import sys

def get_book_text(fpath):
    return fpath.read()

def generate_report(fpath, word_count, char_count_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fpath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in char_count_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

def main():
    fpath=""
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        fpath=sys.argv[1]
    with open(fpath) as f:
        book=get_book_text(f)
        num_words=get_num_words(book)
        generate_report(fpath,num_words,get_num_chars(book))


main()