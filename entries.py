from tkinter import Entry


def setup_entries():
    website_entry = Entry(width=28)
    website_entry.grid(row=1, column=1, sticky="W", columnspan=2, pady=5)
    website_entry.focus()
    username_entry = Entry(width=53)
    username_entry.grid(row=2, column=1, sticky="W", columnspan=2, pady=5)
    password_entry = Entry(width=28)
    password_entry.grid(row=3, column=1, sticky="W", pady=5)

    return {
        "website": website_entry,
        "username": username_entry,
        "password": password_entry,
    }