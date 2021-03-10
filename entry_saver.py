def save_entry(website, username, password):
    with open("data.csv", "a") as data_file:
        data_file.write(f"{website},{username},{password}\n")
