from cryptography.fernet import Fernet
import os

 
def encrypt(string):
    #Read the generated key
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    f = Fernet(key)
    encrypted = f.encrypt(string.encode())
    return encrypted
