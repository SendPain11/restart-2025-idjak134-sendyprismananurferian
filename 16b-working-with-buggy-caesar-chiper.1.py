# Module Lab: Caesar Cipher Program Bux 2- Case Sensitive Version
# Modified to preserve Uppercase and Lowercase letters

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
    
    # [PERUBAHAN 1] Jangan gunakan .upper() pada seluruh kalimat di sini.
    # Gunakan loop langsung ke 'message' asli agar kita tahu huruf asli user.
    for currentCharacter in message:
        
        # [PERUBAHAN 2] Cek status: Apakah huruf ini huruf kecil?
        is_lower = currentCharacter.islower()
        
        # [PERUBAHAN 3] Ubah ke Kapital SEMENTARA hanya untuk mencari indeks di 'alphabet'
        # (Karena variabel 'alphabet' isinya huruf besar semua: ABC...)
        temp_upper_char = currentCharacter.upper()
        position = alphabet.find(temp_upper_char)
        
        # Jika position ditemukan (artinya dia huruf A-Z)
        if position != -1:
            newPosition = position + int(cipherKey)
            
            # Ambil karakter baru yang sudah digeser
            newChar = alphabet[newPosition]
            
            # [PERUBAHAN 4] LOGIKA PENGEMBALIAN CASING
            # Jika aslinya huruf kecil, maka hasil enkripsinya kita kecilkan lagi.
            if is_lower:
                newChar = newChar.lower()
                
            encryptedMessage = encryptedMessage + newChar
        else:
            # Jika karakter tidak ada di alphabet (spasi, tanda baca, angka)
            encryptedMessage = encryptedMessage + currentCharacter
            
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
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