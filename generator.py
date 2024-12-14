

import random

def generate_password(password_length=12):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
    password = ''

    for x in range(password_length):
        password += random.choice(chars)

    return password
