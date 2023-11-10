#Password
import random
import string

def generate_password(lengeth):
    character=string.ascii_letters + string.digits + string.punctuation
    password='' .join(random.choice(character) for _ in range(lengeth))
    return password
def password_generator():
    try:
        length = int(input("Enter the desired length of the password:"))

        if length <=0:
            print("Please enter a positive length.")
            return
            
        password = generate_password(length)
        print(f"Generate Password: {password}")
    
    except ValueError:
       print("Invalid input. Please enter a valid number for the ")

if __name__=="__main__":
   password_generator
