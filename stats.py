def num_of_words(text_from_book):
    num_of_words = 0
    words = text_from_book.split()
    for word in words:
        num_of_words += 1
    print(f"{num_of_words} words found in the document")

def num_of_characters(text_from_book):
    character_count = {}
    words = text_from_book.lower()
    for character in words:
        check = character in character_count
        if check == True:
            character_count[character] += 1
        else:
            character_count[character] = 1
    print (character_count)
    

