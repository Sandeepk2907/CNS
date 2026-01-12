import re
def password_strength(password):
    if len(password)<8:
     print("Password is Too short")
    elif not re.search("[a-z]",password):
        print("Password should Have atleast one Lowercase Letter")
    elif not re.search("[A-Z]",password):
         print("Password should Have atleast one uppercase Letter")
    elif not re.search("[0-9]",password):
        print("Password should have atleast one digit")
    elif not re.search("[!@#$%^&*()<>|}{]",password):
         print("Password should Have atleast one special character")
    else:
        print("Password is Strong")
user_password=input("ENter A Password to check its strength:")
password_strength(user_password)        
        