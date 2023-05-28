import base64
import hashlib
from Crypto.Cipher import DES

password = "Password"
salt = b"\x28\xAB\xBC\xCD\xDE\xEF\x00\x33"

key = password.encode() + salt
m = hashlib.md5(key)
key = m.digest()
dk, iv = key[:8], key[8:]

crypter = DES.new(dk, DES.MODE_CBC, iv)

plain_text = "I see you"
print("The plain text is:", plain_text)

plain_text += b'\x00' * (8 - len(plain_text) % 8)
ciphertext = crypter.encrypt(plain_text)
encoded_string = base64.b32encode(ciphertext).decode()
print("The encoded string is:", encoded_string)