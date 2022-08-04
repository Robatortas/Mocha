import os
from cryptography.fernet import Fernet

def getChocoContents():
    with open("choco.mocha", "rb") as choco:
        key = choco.read()
        return key
        
def decrypt(file):
    with open(file, "rb") as choco:
        loneKey = choco.read()
        decrypted = Fernet(getChocoContents()).decrypt(loneKey)
    with open(file, "wb") as final:
        final.write(decrypted)
        
for file in os.listdir():
    if file == "mocha.py" or file == "cappuccino.py" or file == "choco.mocha":
        continue
    if os.path.isfile(file):
        decrypt(file)
        