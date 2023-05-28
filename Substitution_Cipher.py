def generation_of_key():
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = input("Enter the words for Substitution in order: ")
    return dict(zip(plaintext, ciphertext))

def substitution_cipher(text, key):
    result = ''
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += key[char.upper()]
            else: 
                result += key[char.upper()].lower()
        else:
            result += char
    
    print(result)
    
txt = input("Enter the Plain-Text: ")
k = generation_of_key()

substitution_cipher(txt, k)