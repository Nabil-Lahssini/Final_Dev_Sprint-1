from cryptography.fernet import Fernet
import os

 

#generate a new key to the key.key file
def generate_key():
    os.remove('key.key')
    key = Fernet.generate_key()
    file = open('key.key', 'wb')  # Open the file as wb to write bytes
    file.write(key)
    file.close()

 

generate_key()

 
def encrypt(string):
    #Read the generated key
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    f = Fernet(key)
    f.encrypt(string.encode())