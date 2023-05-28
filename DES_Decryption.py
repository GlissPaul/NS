import base64
import hashlib
from Crypto.Cipher import DES

password = "Password"
salt = b' \x28\xAB\xBC\xCD\xDE\xEF\x00\x33'

key = password.encode() + salt
m = hashlib.md5(key)
key = m.digest()
dk, iv = key[:8], key[8:]

crypter = DES.new(dk, DES.MODE_CBC, iv)

encrypted_string = 'UH562EGM8RCHHTOUC5CTRS590G======'
print("The encrypted string is:", encrypted_string)

encrypted_string = base64.b32decode(encrypted_string)
decrypted_string = crypter.decrypt(encrypted_string)
decrypted_string = decrypted_string.rstrip(b'\x00').decode()
print("The decrypted string is:", decrypted_string)