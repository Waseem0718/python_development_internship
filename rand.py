import random
import string

def generate_password(length):
    
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def randompasswordgenertor():
    while True:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Invalid number,Enter length more than 0")
        else:
             print("Generated Password:", generate_password(length))
             break

            
randompasswordgenertor()