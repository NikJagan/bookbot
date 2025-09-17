def num_of_words(text_from_book):
    num_of_words = 0
    words = text_from_book.split()
    for word in words:
        num_of_words += 1
    return (f"Found {num_of_words} total words")

def num_of_characters(text_from_book):
    character_count = {}
    words = text_from_book.lower()
    for character in words:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return (character_count)

def char_num_split(character_count):
    result = []
    for ch, num in character_count.items():
        if ch.isalpha():
            result.append({"char": ch, "num": num})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(item):
    return item["num"]
    
    
    

    

