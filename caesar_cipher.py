# Define the alphabet used for encryption and decryption
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Store the total number of letters (26)
num_letters = len(alphabet)


# Function to ENCRYPT plaintext using Caesar Cipher
def encrypt(plaintext, key):
    ciphertext = ''  # Stores encrypted result

    # Loop through each character in the input text
    for ch in plaintext:
        ch = ch.lower()  # Convert character to lowercase for consistency

        # Check if character is a letter
        if ch in alphabet:
            index = alphabet.find(ch)               # Find letter position
            new_index = (index + key) % num_letters # Shift forward with wrap-around
            ciphertext += alphabet[new_index]      # Add encrypted letter
        else:
            ciphertext += ch  # Keep spaces, numbers, symbols unchanged

    return ciphertext


# Function to DECRYPT ciphertext using Caesar Cipher
def decrypt(ciphertext, key):
    plaintext = ''  # Stores decrypted result

    # Loop through each character in the encrypted text
    for ch in ciphertext:
        ch = ch.lower()

        # Check if character is a letter
        if ch in alphabet:
            index = alphabet.find(ch)               # Find letter position
            new_index = (index - key) % num_letters # Shift backward with wrap-around
            plaintext += alphabet[new_index]       # Add decrypted letter
        else:
            plaintext += ch  # Keep spaces, numbers, symbols unchanged

    return plaintext


# ---------------- MAIN PROGRAM ----------------

print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

# Ask user for mode selection
print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

# Encryption mode
if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()

    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')

    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

# Decryption mode
elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()

    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')

    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')

