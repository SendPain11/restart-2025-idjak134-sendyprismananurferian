# Module Lab: Caesar Cipher Program Bug #3 FIXED (Case Sensitive)
#
# In a previous lab, you created a Caesar cipher program. This version of
# the program is buggy. Use a debugger to find the bug and fix it.

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Get a message to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Get a cipher key
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    
    # [PERBAIKAN CASE SENSITIVITY]
    # Hapus 'uppercaseMessage = message.upper()'
    # Kita loop langsung ke pesan asli 'message'
    for currentCharacter in message:
        
        # 1. Simpan status: apakah huruf aslinya kecil?
        is_lower = currentCharacter.islower()
        
        # 2. Ubah ke kapital SEMENTARA untuk mencari posisi di variabel 'alphabet'
        temp_upper_char = currentCharacter.upper()
        position = alphabet.find(temp_upper_char)
        
        # 3. Proses Geser
        if position != -1: # Jika ditemukan di alfabet
            newPosition = position + int(cipherKey)
            newChar = alphabet[newPosition]
            
            # 4. Kembalikan ke huruf kecil jika aslinya memang kecil
            if is_lower:
                newChar = newChar.lower()
                
            encryptedMessage = encryptedMessage + newChar
        else:
            # Jika bukan huruf (spasi, angka, simbol), biarkan saja
            encryptedMessage = encryptedMessage + currentCharacter
            
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    
    # [PERBAIKAN LOGIKA DECRYPT]
    # Menggunakan decryptKey, BUKAN cipherKey
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(f'Original Message: {myMessage}')
    myCipherKey = getCipherKey()
    print(f'Key: {myCipherKey}')
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram()