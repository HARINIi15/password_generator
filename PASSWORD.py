import random

import string

 

def generate_password(length):

    

    characters = string.ascii_letters + string.digits + string.punctuation

   

    
    password = ''.join(random.choice(characters) for _ in range(length))

   

    return password

 

def main():

    user_name = input("Enter your name: ")

    print(f"Welcome, {user_name}, to the Password Generator!")

   

    

    while True:

        try:

            length = int(input("Enter the desired password length: "))

            if length <= 0:

                print("Please enter a positive integer for the length.")

            else:

                break

        except ValueError:

            print("Please enter a valid integer for the length.")

 

    
    password = generate_password(length)

    print(f"Generated Password for {user_name}: {password}")

 

if __name__ == "__main__":

    main()