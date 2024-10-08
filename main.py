import customtkinter as ctk # pip3 install customtkinter
from tkinter import filedialog # pip3 install tk

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

def choose_document():
    file_location = filedialog.askopenfilename()
    book_path_entry.delete(0, ctk.END)
    book_path_entry.insert(0, file_location)

def analyze():
    result_label.configure(text="test", font=("Roboto", 15))
    book_path = book_path_entry.get()
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

# create window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Bookbot")
root.geometry("500x500")

# set layout
file_text = ctk.CTkLabel(root, text="Choose the location of your document", font=("Roboto",24))
file_text.pack(padx=10, pady=10)

book_path_entry = ctk.CTkEntry(root, width=400)
book_path_entry.pack(padx=10, pady=10)

choose_file = ctk.CTkButton(root, text="Choose file", font=("Roboto", 15), command=choose_document)
choose_file.pack(padx=10, pady=10)

proceed_text = ctk.CTkLabel(root, text="Proceed with the analysis", font=("Roboto", 24))
proceed_text.pack(padx=10, pady=(30,10))

analyze_button = ctk.CTkButton(root, text="Analyze", font=("Roboto", 15), command=analyze)
analyze_button.pack(padx=10, pady=10)

result_text = ctk.CTkLabel(root, text="Results", font=("Roboto", 24))
result_text.pack(padx=10, pady=(20, 10))

result_label = ctk.CTkLabel(root, text="", font=("Roboto", 15))
result_label.pack(padx=10, pady=10)

root.mainloop()