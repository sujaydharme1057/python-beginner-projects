import string
import random

charcters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the length of Password you want: "))

if length < 4:
    print("Password length must be at least 4.")

else:
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    password = [uppercase, lowercase, number, symbol]

    remaining = length - 4

    for i in range(remaining):
        password.append(random.choice(charcters))

    random.shuffle(password)

    password = "".join(password)

    print("Your Password:", password)