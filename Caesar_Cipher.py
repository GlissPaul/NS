def caesar_cipher(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)  # Shifting uppercase letters
            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)  # Shifting lowercase letters
        else:
            result += char  # Retain non-alphabetic characters

    print(result)
    

txt = input("Enter the Plain-Text: ")
k = int(input("Enter the Number; "))

caesar_cipher(txt, k)