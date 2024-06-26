import re

def strong_password(password):
    
    if len(password) < 8:
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[!@#$%^&*()-_=+{};:,<.>]", password):
        return False
    
    return True

# Test the function

print("GUIDELINES FOR STRONG PASSWORD :")
print("1.The password must be at least 8 characters long.")
print("2.The password must contain at least one uppercase letter.")
print("3.The password must contain at least one lowercase letter.")
print("4.The password must contain at least one digit.")
print("5.The password must contain at least one special character.\n")

while True:
 password1 = input("ENTER PASSWORD: ")
 if strong_password(password1):
   print("STRONG PASSWORD DETECTED.")
   break
 else:
   print("Weak Password Detected, Please Enter Strong Password.")    