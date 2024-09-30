import customtkinter as ctk # type: ignore

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars_dict = count_characters(text)
    sorted_list = dict_to_list(chars_dict)

    print(f"--- Report of {book_path} ---")
    print(f"This file contains {words} words.")
    print()
    print("Occurence of each character:")

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"Letter '{item['char']}' spotted {item['num']} times.")

    print("--- End ---")

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

def sort_on(dict):
    return dict["num"]
    
def dict_to_list(dict):
    sorted_list = []
    for d in dict:
        sorted_list.append({"char":d, "num":dict[d]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# create window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Bookbot")
root.geometry("500x500")

root.mainloop()