from cryptography.fernet import Fernet
import os
# !!! DON'T GENERATE A NEW KEY IF ALREADY DONE. OTHERWISE ALL THE DATA WILL BE LOST !!!
# !!! DON'T GENERATE A NEW KEY IF ALREADY DONE. OTHERWISE ALL THE DATA WILL BE LOST !!!
# !!! DON'T GENERATE A NEW KEY IF ALREADY DONE. OTHERWISE ALL THE DATA WILL BE LOST !!!
# !!! DON'T GENERATE A NEW KEY IF ALREADY DONE. OTHERWISE ALL THE DATA WILL BE LOST !!!
# !!! DON'T GENERATE A NEW KEY IF ALREADY DONE. OTHERWISE ALL THE DATA WILL BE LOST !!!
# !!! DON'T GENERATE A NEW KEY IF ALREADY DONE. OTHERWISE ALL THE DATA WILL BE LOST !!!

#generate a new key to the key.key file
def generate_key():
    key = Fernet.generate_key()
    file = open('key.key', 'wb')  # Open the file as wb to write bytes
    file.write(key)
    file.close()
generate_key()