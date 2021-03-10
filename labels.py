from constants import BACKGROUND_COLOR, FOREGROUND_COLOR, LBL_FONT
from tkinter import Label


def setup_labels():
    website_label = Label(text="Website:", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=LBL_FONT)
    website_label.grid(row=1, column=0, sticky="W")
    username_label = Label(text="Username:", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=LBL_FONT)
    username_label.grid(row=2, column=0, sticky="W")
    password_label = Label(text="Password:", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=LBL_FONT)
    password_label.grid(row=3, column=0, sticky="W")
