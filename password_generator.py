from random import randint, choice, shuffle
import string

# -------------------------- LISTS SETUP --------------------------------- #
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
symbols = list(string.punctuation)
numbers = list(string.digits)


# ---------------------------- METHODS ----------------------------------- #
def generate_password(n_upper_letters=None, n_lower_letters=None, n_symbols=None, n_numbers=None):
    if not n_upper_letters:
        n_upper_letters = randint(4, 6)
    if not n_lower_letters:
        n_lower_letters = randint(4, 6)
    if not n_symbols:
        n_symbols = randint(2, 4)
    if not n_numbers:
        n_numbers = randint(2, 4)

    list_upper_letters = [choice(uppercase_letters) for _ in range(n_upper_letters)]
    list_lower_letters = [choice(lowercase_letters) for _ in range(n_lower_letters)]
    list_symbols = [choice(symbols) for _ in range(n_symbols)]
    list_numbers = [choice(numbers) for _ in range(n_numbers)]

    password_list = list_upper_letters + list_lower_letters + list_symbols + list_numbers
    shuffle(password_list)
    password = "".join(password_list)

    return password
