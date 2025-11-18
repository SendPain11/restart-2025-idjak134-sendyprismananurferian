# Import the necessary modules
import os
import subprocess

# --- Exercise 1: Using os.system ---
print("\n--- Exercise 1: os.system('ls') ---")
# os.system is simple but less powerful. It just runs the command string.
os.system("ls")


# --- Exercise 2: Using subprocess.run ---
print("\n--- Exercise 2: subprocess.run(['ls']) ---")
# subprocess.run is newer and recommended. It takes a list of arguments.
subprocess.run(["ls"])


# --- Exercise 3: subprocess.run with arguments ---
print("\n--- Exercise 3: subprocess.run(['ls', '-l']) ---")
# Adding '-l' creates a long listing format (details about permissions, size, etc.)
subprocess.run(["ls", "-l"])


# --- Exercise 4: subprocess.run with three arguments ---
print("\n--- Exercise 4: subprocess.run(['ls', '-l', 'README.md']) ---")
# Listing details for a specific file (README.md)
# Note: If README.md doesn't exist, this might show an error message from ls.
subprocess.run(["ls", "-l", "README.md"])


# --- Exercise 5: Retrieving system information (uname) ---
print("\n--- Exercise 5: System Info (uname -a) ---")
# We use variables to make the code cleaner and more dynamic
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])


# --- Exercise 6: Retrieving process information (ps) ---
print("\n--- Exercise 6: Process Info (ps -x) ---")
# 'ps' shows process status. '-x' shows processes not attached to a terminal.
# Note: The lab title mentions "disk space" (df) but the instruction code uses "ps".
# We follow the instruction code here.
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])