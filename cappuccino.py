import os
from cryptography.fernet import Fernet

# Cappuccino is for the file decryption.

files = []

def getChocoContents():
    with open("choco.mocha", "rb") as choco:
        key = choco.read()
        return key

for file in os.listdir():
    if file == "mocha.py":
        continue
     
    #print(getChocoContents())
    
def decryptFiles():
    