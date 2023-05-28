import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt(message, key):
  cipher = Cipher(algorithms.AES(key), modes.ECB())
  encrypted_message = cipher.encryptor().update(message) + cipher.encryptor().finalize()
  print(base64.b64encode(encrypted_message))

def decrypt(encrypted_message, key):
  cipher = Cipher(algorithms.AES(key), modes.ECB())
  decrypted_message = cipher.decryptor().update(base64.b64decode(encrypted_message)) + cipher.decryptor().finalize()
  print(decrypted_message)

message = "This is a secret message."
key = os.urandom(16)
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
