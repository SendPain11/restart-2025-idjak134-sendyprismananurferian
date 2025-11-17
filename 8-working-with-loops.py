# --- BAGIAN 1: IMPORT LIBRARY ---
import random

# --- BAGIAN 2: LATIHAN WHILE LOOP (GAME TEBAK ANGKA) ---
print("=== LATIHAN 1: WHILE LOOP (GAME TEBAK ANGKA) ===")
print("Selamat datang di Tebak Angka!")
print("Aturannya sederhana. Saya memikirkan angka 1-10, coba tebak ya.")

# Komputer memilih angka acak
number = random.randint(1,10)

# Variabel kontrol
isGuessRight = False

# Memulai Loop
while isGuessRight != True:
    guess = input("Tebak angka antara 1 sampai 10: ")
    
    if int(guess) == number:
        print("Tebakan Anda {}. Benar! Anda Menang!".format(guess))
        isGuessRight = True # Ini akan menghentikan loop while
    else:
        print("Tebakan Anda {}. Salah, coba lagi.".format(guess))

# --- JEDA ANTAR LATIHAN ---
print("\n" + "="*40)
input("Tekan ENTER untuk lanjut ke Latihan 2...")
print("="*40 + "\n")

# --- BAGIAN 3: LATIHAN FOR LOOP (BERHITUNG) ---
print("=== LATIHAN 2: FOR LOOP (BERHITUNG) ===")
print("Mari berhitung sampai 10!")

# Memulai For Loop
for x in range (0, 11):
    print(x)

print("\nSelesai! Semua latihan berhasil dijalankan.")