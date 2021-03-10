from tkinter import *
from logo import Logo
from constants import BACKGROUND_COLOR
from labels import setup_labels
from entries import setup_entries
from generate_button import GeneratePasswordBtn
from add_entry_button import AddButton


def main():
    window = Tk()
    window.title("MyPass - Password Manager")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    logo_img = PhotoImage(file="./logo.png")
    Logo(logo_img)
    setup_labels()
    entries = setup_entries()
    GeneratePasswordBtn(entries)
    AddButton(entries)

    window.mainloop()


if __name__ == "__main__":
    main()
