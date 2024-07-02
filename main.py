# def main():
#     book_path = "books/frankenstein.txt"
#     with open(book_path) as f:
#         file_contents = f.read()
#     print(file_contents)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars_dict = count_characters(text)
    print(f"This book contains {words} words.")
    print("Occurence of each character:")
    print(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered not in characters:
            characters[lowered] = 1
        else:
            characters[lowered] += 1
    return characters

    
main()