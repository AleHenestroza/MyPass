from tkinter import Button, END
from password_generator import generate_password
from constants import BUTTON_COLOR, BTN_FONT, FOREGROUND_COLOR


class GeneratePasswordBtn(Button):

    def __init__(self, pass_entry):
        super().__init__(
            text="Generate Password",
            bg=BUTTON_COLOR,
            fg=FOREGROUND_COLOR,
            highlightthickness=0,
            font=BTN_FONT,
            command=self.generate
        )
        self.pass_entry = pass_entry
        self.grid(row=3, column=2, sticky="W", padx=5)

    def generate(self):
        self.pass_entry.delete(0, END)
        self.pass_entry.insert(0, generate_password())
        self.clipboard_clear()
        self.clipboard_append(self.pass_entry.get())

