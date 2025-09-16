def num_of_words(text_from_book):
    num_of_words = 0
    words = text_from_book.split()
    for word in words:
        num_of_words += 1
    print(f"{num_of_words} words found in the document")