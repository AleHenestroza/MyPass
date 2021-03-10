from tkinter import *
from logo import Logo
from constants import BACKGROUND_COLOR
from labels import setup_labels
from entries import setup_entries
from generate_button import GeneratePasswordBtn
from add_entry_button import AddButton

# TODO-1 Let the user retrieve their passwords easily from the application instead of having to open the .csv file
# TODO-2 Let the user input a preferred password length for the random password generator
# TODO-3 Let the user decide how many uppercase or lowercase letters, as well as symbols and numbers, are in a password
# TODO-4 Change storage from .csv to use a database with basic encryption
# TODO-5 Tweak User Interface to make it look good


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
