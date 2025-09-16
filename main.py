from stats import num_of_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(x):
    y = get_book_text(x)
    z = num_of_words(y)

main("/home/neonik21/workspace/github.com/NikJagan/bookbot/books/frankenstein.txt")


