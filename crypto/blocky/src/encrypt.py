import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Read image data
with open(sys.argv[1], 'rb') as f:
    plaintext_bytes = pad(f.read(), 16)

# Generate a random key
key = get_random_bytes(32)

# Encrypt image data
cipher = AES.new(key, AES.MODE_ECB)
ciphertext_bytes = cipher.encrypt(plaintext_bytes)

# Write encrypted image data
with open(sys.argv[1] + '.enc', 'wb') as f:
    f.write(ciphertext_bytes)