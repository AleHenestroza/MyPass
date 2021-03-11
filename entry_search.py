import json
from tkinter import messagebox


def search_entry(text_to_match):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if text_to_match in data:
                return data[text_to_match]
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="There is no data file.\n"
                                                   "This may be because it's the first time you use this program.\n"
                                                   "Try saving some entries before using the search button.")
        return None
    return -1  # Código para cuando no hay match
