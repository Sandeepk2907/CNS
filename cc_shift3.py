def caesar_cipher_encrypt(plain_text,shift):
    encrypted=" "
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encrypted_char=chr((ord(char)-ord('A')+shift)%26+ord('A'))
            else:
                encrypted_char=chr((ord(char)-ord('a')+shift)%26+ord('a'))
            encrypted+=char
        else:
            encrypted+=char
    return encrypted
plain_text=input("Enter The Plaintext:")
shift=int(input("Enter the shift value:"))
encrypted_text=caesar_cipher_encrypt(plain_text,shift)
print("Encrypted Text:",encrypted_text)