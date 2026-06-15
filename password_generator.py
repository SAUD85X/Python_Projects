#password generator

import random
import string

def generate_password(length):
    character = string.ascii_letters +string.digits + string.punctuation
    password =''.join(random.choice(character) for _ in range(length))
    return password

print("✨ Password Generator")
#ask user for password length
length=int(input("Enter the length of the password:"))

password =generate_password(length)
print("\n you secured password:",password)
print("password genearted succesively!")


