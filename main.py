# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)

# def get_book_text(path):
#     with open(path) as f:
#         return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    print(file_contents)

main()