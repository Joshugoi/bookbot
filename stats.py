
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


def sort_char(text):
    for key, value in count_letters(text).items():
        print(f" {key}: {value} ")