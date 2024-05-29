import random
import string 
chars=" "+string.digits+string.punctuation+string.ascii_letters #instead of typing all manually
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#decyption
cipher_text=input("Enter a message to decrypt")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]
    
print(f"encrypted message: {cipher_text}")
print(f"original message was: {plain_text}")