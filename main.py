from stats import *

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

word_count, sorted_chars = main("/home/neonik21/workspace/github.com/NikJagan/bookbot/books/frankenstein.txt")

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(word_count)
