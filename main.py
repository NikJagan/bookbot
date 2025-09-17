import sys
from stats import *

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(x):
    text = get_book_text(x)
    word_count = num_of_words(text)
    x = num_of_characters(text)
    sorted_chars = char_num_split(x)
    return word_count, sorted_chars

word_count, sorted_chars = main(sys.argv[1])

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(word_count)
print("--------- Character Count -------")
for item in sorted_chars:
    print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")
