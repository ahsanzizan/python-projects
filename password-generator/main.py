import string
import random

char = list(string.ascii_letters + string.digits + '$#^&*@')


def generate_password(password_length):
    res = ''
    for i in range(password_length):
        res += char[random.randint(0, len(char))]
    return res


print(f"Generated Password: {generate_password(int(input('How long would you like the password to generate > ')))}")
