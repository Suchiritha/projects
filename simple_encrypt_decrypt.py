import base64

# Encrypt Function
def encrypt(text):
    encoded = base64.b64encode(text.encode())
    return encoded.decode()

# Decrypt Function
def decrypt(text):
    decoded = base64.b64decode(text.encode())
    return decoded.decode()

# Main Program
print("---- Simple Encryption & Decryption Tool ----")

message = input("Enter your message: ")

# Encrypt the message
encrypted_text = encrypt(message)
print("\nEncrypted Message:", encrypted_text)

# Decrypt the message
decrypted_text = decrypt(encrypted_text)
print("Decrypted Message:", decrypted_text)
