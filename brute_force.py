def brute_force(password_list,target):
    for password in password_list:
        print(f"Trying Password:{password}")
        
        if password==target:
            print(f"Password Found:{password}")
            return True
    print("Password Not Found")
    return False
if __name__=="__main__":
    password_list=[
        "123456","password","123456789",
        "qwerty","abc123","monkey","letmein",
        "dragon","11111","baseball"
    ]
    target=input("Enter The Password:")
    print("Starting brute force attack...")
    success=brute_force(password_list,target)
    if success:
        print("Brute Force Attack successful!")
    else:
        print("Brute force Attack Failed!!!")