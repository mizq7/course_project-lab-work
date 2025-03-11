# Step 1: Define the Caesar Cipher encryption function
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensures that the shift wraps around after 'Z'
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            encrypted_text += new_char.upper() if char.isupper() else new_char
        else:
            encrypted_text += char
    return encrypted_text

# Step 2: Define the Caesar Cipher decryption function
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Reverse the shift to decrypt

# Step 3: Take user input for the message and shift value
message = input("Enter the message to encrypt: ")
shift = int(input("Enter shift value (e.g., 3): "))

# Step 4: Perform encryption and decryption
encrypted_message = caesar_cipher_encrypt(message, shift)
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)

# Step 5: Display results
print("\nOriginal Message: ", message)
print("Encrypted Message: ", encrypted_message)
print("Decrypted Message: ", decrypted_message)
Pring ("Hello World"
       "")