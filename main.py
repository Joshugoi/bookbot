from stats import *
import sys


def main():
    #print(get_book_text())
    #print(f' {count_words(get_book_text())} words found in the document')
    #print(count_letters(get_book_text()))
    #letter_counts = count_letters(get_book_text())

    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        print(f'--- Begin report of {book_path} ---')
        print(f' Found {count_words(get_book_text(book_path))} total words')
        print (sort_char(get_book_text(book_path)))
        print('--- End report ---') 
        sys.exit(0)
        
    else:
        len(sys.argv) < 2
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()