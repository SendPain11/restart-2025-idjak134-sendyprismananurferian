# Materi Caesar - Cipher
# Exercise 1: Create the Double Alphabet
# This creates a string like "ABC...ZABC...Z" so we can shift letters past 'Z' 
# without getting an "index out of bounds" error.
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Exercise 2: Get the Message
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Exercise 3: Get the Cipher Key
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Exercise 4: Encrypt the Message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    # Convert to uppercase to match our alphabet string
    uppercaseMessage = message.upper()
    
    for currentCharacter in uppercaseMessage:
        # Find where the character is in the alphabet (0-25)
        position = alphabet.find(currentCharacter)
        
        # Calculate the new position by adding the key
        newPosition = position + int(cipherKey)
        
        # If the character is in our alphabet, append the new shifted character
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            # If it's a space or punctuation, just append it without changing it
            encryptedMessage = encryptedMessage + currentCharacter
            
    return encryptedMessage

# Exercise 5: Decrypt the Message
# We reuse the encryption logic but multiply the key by -1 to shift backwards
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Exercise 6: Main Function
def runCaesarCipherProgram():
    # Define the standard alphabet
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    # Create the double alphabet for shifting
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    # Get inputs
    myMessage = getMessage()
    print(myMessage)
    
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    # Encrypt
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    # Decrypt (to prove it works)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Call the main function to start the program
runCaesarCipherProgram()