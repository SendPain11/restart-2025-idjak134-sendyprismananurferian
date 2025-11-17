# --- BAGIAN 1: IMPORT LIBRARY ---
import random

# --- BAGIAN 2: LATIHAN WHILE LOOP (GAME TEBAK ANGKA) ---
print("=== Exercises 1: WHILE LOOP (GUES THE NUMBERS GAME) ===")
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Komputer memilih angka acak
number = random.randint(1,10)

# Variabel kontrol
isGuessRight = False

# Memulai Loop
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

# --- JEDA ANTAR LATIHAN ---
print("\n" + "="*40)
input("Push ENTER for next to Exercises 2...")
print("="*40 + "\n")

# --- BAGIAN 3: LATIHAN FOR LOOP (BERHITUNG) ---
print("=== Exercises 2: FOR LOOP (COUNTING) ===")
print("Let's Go Count to 10!")

# Memulai For Loop
for x in range (0, 11):
    print(x)

print("\nYou are to Finish!")