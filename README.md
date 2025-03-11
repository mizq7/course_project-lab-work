# Caesar Cipher Encryption Lab

# Step 1: Open a Python Environment
You can use a Python IDE (such as PyCharm or VS Code) or run Python in the terminal/command prompt.

# Step 2: Write the Caesar Cipher Code
Create a new Python file (caesar_cipher.py) and copy the following code into it:

# Step 3: Caesar Cipher Decryption Function (Run the following code)
def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = (-shift) % 26  
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            decrypted_text += new_char.upper() if char.isupper() else new_char
        else:
            decrypted_text += char
    return decrypted_text

# Get Encrypted Message from Email
encrypted_message = input("Enter the encrypted message you received: ")
shift_value = int(input("Enter the shift value provided in the email: "))

# Decrypt the Message
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift_value)

# Display Output
print("\nEncrypted Message: ", encrypted_message)
print("Decrypted Message: ", decrypted_message)

# Running the Script in Terminal

Step 1: Open Terminal or Command Prompt
For macOS/Linux: Open Terminal.
For Windows: Open Command Prompt (cmd) or PowerShell.

# Step 4: Navigate to Your Project Folder
Use the cd command to move into the directory where you saved the caesar_cipher.py file.

If your folder name contains spaces, use:
**(copy the following code)**

cd "Your/Project/Folder/Path"
If your folder name has spaces, escape them with a backslash ():
**(copy the following code)**

cd Your/Project/Folder\ Path/

# Step 5: Verify You Are in the Correct Directory
Run:

**(copy the following code)**

pwd
Expected Output: The path of your project folder should be displayed.

# Step 6: Run Your Python Script
Execute the script by running:
**(copy the following code)**

python3 caesar_cipher.py
(Use python instead of python3 if your system uses Python 2 by default.)

# Step 7: Enter Input for Encryption
When prompted, enter a message and a shift value.

Example Input:
Enter the message to encrypt: Hello World
Enter shift value (e.g., 3): 3

Expected Output:

Original Message:  Hello World

Encrypted Message:  Khoor Zruog

Decrypted Message:  Hello World

# How It Works
The Caesar Cipher shifts each letter forward by the shift value (e.g., 3 shifts ‘H’ to ‘K’).
Non-alphabetic characters (spaces, punctuation) remain unchanged.
The decryption reverses the shift, restoring the original message.
This process demonstrates a simple encryption technique used historically to encode secret messages.
