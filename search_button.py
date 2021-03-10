from tkinter import Button, messagebox
from constants import BUTTON_COLOR, BTN_FONT, FOREGROUND_COLOR
from entry_search import search_entry


class SearchButton(Button):

    def __init__(self, website):
        super().__init__(
            text="Search",
            width=17,
            bg=BUTTON_COLOR,
            fg=FOREGROUND_COLOR,
            highlightthickness=0,
            font=BTN_FONT,
            command=self.search
        )
        self.website = website
        self.grid(row=1, column=2, sticky="W", padx=5)

    def search(self):
        web_entry = self.website.get()
        if not web_entry:
            messagebox.showwarning(title="Invalid search", message="You must enter a website before searching.")
        else:
            entry = search_entry(web_entry)
            if entry:
                if entry == -1:
                    messagebox.showwarning(title="No matches", message="No match could be found for your search term.")
                else:
                    values = []
                    for key, value in entry.items():
                        values.append(value)
                    username = values[0]
                    password = values[1]
                    messagebox.showinfo(title=web_entry, message=f"Username: {username}\nPassword: {password}")
