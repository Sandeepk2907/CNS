import hashlib
target=input("Enter The Target Password:")
hash=hashlib.md5(target.encode()).hexdigest()

passwords=[
    '123456',
    'password',
    'password123',
    'admin'
]
def crack_hash(hash,dictionary):
    for p in dictionary:
        hashed_password=hashlib.md5(p.encode()).hexdigest()
        if hashed_password==hash:
            print(f"Password Found:{p}")
            return p
        print("Password Not Found!!!")
        return None
crack_hash(hash,passwords)