from tkinter import Button, messagebox, END
from constants import BUTTON_COLOR, BTN_FONT, FOREGROUND_COLOR
from entry_saver import save_entry


class AddButton(Button):

    def __init__(self, entries):
        super().__init__(
            text="Add Entry",
            bg=BUTTON_COLOR,
            fg=FOREGROUND_COLOR,
            highlightthickness=0,
            font=BTN_FONT,
            command=self.add_entry
        )
        self.entries = entries
        self.grid(row=4, column=1, sticky="E", pady=15)

    def add_entry(self):
        is_ok_to_save = True
        values = []
        for key, value in self.entries.items():
            if not value.get():
                messagebox.showerror(title="Invalid input", message="One or more fields are empty.")
                is_ok_to_save = False
                break
            else:
                values.append(value.get())
        if is_ok_to_save:
            save_entry(values[0], values[1], values[2])
            messagebox.showinfo(title="Success", message="The new entry has been saved.")
            for key, value in self.entries.items():
                value.delete(0, END)
