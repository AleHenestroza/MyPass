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
        website_text = self.website.get().title()
        if not website_text:
            messagebox.showwarning(title="Invalid search", message="You must enter a website before searching.")
        else:
            entry = search_entry(website_text)
            if entry:
                messagebox.showinfo(title=website_text, message=f"Username: {entry['Username']}\n"
                                                                f"Password: {entry['Password']}")
