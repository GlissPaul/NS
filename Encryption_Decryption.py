def encrypt(message, key):
    encryption_message = ''
    for char in message:
        encrypted_char = chr(ord(char) + key)
        encryption_message += encrypted_char
    return encryption_message 
 
def decrypt(encryption_message, key):
    decryption_message = ''
    for char in encryption_message:
        decrypted_char = chr(ord(char) - key)
        decryption_message += decrypted_char
    return decryption_message
    
message = input()
key = int(input())

encryption_message = encrypt(message, key)
decryption_message = decrypt(encryption_message, key)
print("Encryption Message: ", encryption_message)
print("Decryption Message: ", decryption_message)
