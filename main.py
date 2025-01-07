def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = character_count(text)
    print (f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    for (char, count) in characters:
        print (f"The '{char}' character was found {count} times")
    print ("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(text):
    text_string = f"{text}"
    lower_case = text_string.lower()
    count_dict = {}
    for letter in lower_case:
        if letter in count_dict:
            count_dict[f"{letter}"] += 1
        else:
            count_dict[f"{letter}"] = 1
    
    count_list = [(char, count) for char, count in count_dict.items()]
    filtered_count_list = [(char,count) for char,count in count_list if char.isalpha()]
    sorted_count_list = sorted(filtered_count_list, key=lambda x: x[1], reverse=True)
    
    return sorted_count_list


main()



    




