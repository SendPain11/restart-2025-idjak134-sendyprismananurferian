# 1. Membuat Alfabet Ganda
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# 2. Meminta Pesan dari User
def getMessage():
    stringToEncrypt = input("Masukkan pesan (bisa huruf besar/kecil): ")
    return stringToEncrypt

# 3. Meminta Kunci Geser (Key)
def getCipherKey():
    shiftAmount = input("Masukkan kunci (angka 1-25): ")
    return shiftAmount

# 4. Enkripsi Pesan (BAGIAN YANG DIMODIFIKASI)
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    
    # Kita tidak menggunakan message.upper() di sini agar pesan asli terjaga
    for currentCharacter in message:
        
        # Ubah karakter saat ini ke kapital HANYA untuk mencari posisinya di alfabet
        upperChar = currentCharacter.upper()
        position = alphabet.find(upperChar)
        
        # Jika huruf ditemukan di alfabet (posisi tidak -1)
        if position != -1:
            newPosition = position + int(cipherKey)
            newLetter = alphabet[newPosition]
            
            # LOGIKA BARU: Cek apakah huruf aslinya adalah huruf kecil?
            if currentCharacter.islower():
                # Jika ya, ubah hasil enkripsi menjadi kecil juga
                encryptedMessage = encryptedMessage + newLetter.lower()
            else:
                # Jika tidak (berarti kapital), biarkan kapital
                encryptedMessage = encryptedMessage + newLetter
        else:
            # Jika bukan huruf (misal spasi, angka, simbol), biarkan apa adanya
            encryptedMessage = encryptedMessage + currentCharacter
            
    return encryptedMessage

# 5. Dekripsi Pesan
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# 6. Fungsi Utama
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    
    # Input
    myMessage = getMessage()
    myCipherKey = getCipherKey()
    
    # Proses Enkripsi
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Pesan Terenkripsi: {myEncryptedMessage}')
    
    # Proses Dekripsi (Pembuktian)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Pesan Didekripsi : {myDecryptedMessage}')

# Jalankan Program
runCaesarCipherProgram()