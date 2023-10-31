import random
import string

chars  = string.punctuation + string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_lowercase + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Chars {chars}")
print(f"Key {key}")

def Encrypt(plain_text):
    cipher_text = ""
    
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    print("cypher is" + cipher_text)

def Decrypt(cipher_text):
    plain_text = ""
    
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += chars[index]
        
    print("cypher is" + plain_text)

def DecEnc():
    choice = input("Encrypt or Decrypt?")
    text = ""
    
    if choice == Encrypt:
        text = input("Gib Text")
        Encrypt(text)
    else:
        text = input("gib text")
        Decrypt(text)
    

DecEnc()