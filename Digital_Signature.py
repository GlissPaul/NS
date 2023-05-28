import hashlib
import rsa

def generate_keypair():
  """Generates a public/private key pair."""
  p = rsa.generate_prime(2048)
  q = rsa.generate_prime(2048)
  n = p * q
  e = 65537
  d = rsa.inverse(e, (p - 1) * (q - 1))

  public_key = rsa.PublicKey(n, e)
  private_key = rsa.PrivateKey(n, d)

  return public_key, private_key

def sign(message, private_key): 
  
  hash = hashlib.sha256()
  hash.update(message.encode('utf-8'))
  signature = rsa.sign(hash.digest(), private_key, 'SHA-256')

  return signature

def verify(message, signature, public_key):
  """Verifies a signature using a public key."""
  hash = hashlib.sha256()
  hash.update(message.encode('utf-8'))
  return rsa.verify(hash.digest(), signature, public_key, 'SHA-256')

if __name__ == '__main__':
  # Generate a public/private key pair.
  public_key, private_key = generate_keypair()

  # Sign a message.
  message = 'This is a message.'
  signature = sign(message, private_key)

  # Verify the signature.
  assert verify(message, signature, public_key)
