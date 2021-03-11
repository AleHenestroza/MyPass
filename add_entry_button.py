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
        error = False
        for key, value in self.entries.items():
            if not value.get():
                error = True
                break
        if error:
            messagebox.showerror(title="Oops", message="One or more fields are empty.")
        else:
            entries_json = {
                self.entries["website"].get().title(): {
                    "Username": self.entries["username"].get(),
                    "Password": self.entries["password"].get(),
                }
            }
            save_entry(entries_json)
            messagebox.showinfo(title="Success", message="The new entry has been saved.")
            for key, value in self.entries.items():
                value.delete(0, END)
