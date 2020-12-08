## this class will generate a json file with the encrypted data base login info. With the key in a key.key file
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

#Read the generated key
file = open('key.key', 'rb')  
key = file.read()
file.close()
f = Fernet(key)

#get the login information of the DB
user = input("user : ")
password = input("password : ")
host = input("host : ")
database = input("database : ")

#make an array with the input of the user
array = [user,password,host,database]

#make an array with encrypted data 
encrypted_array = ["0","0","0","0"]
i = 0
for value in array:
    encrypted_array[i] = f.encrypt(value.encode())
    i += 1

#writing it down to the json file
json_content = '"user":"{}", "password":"{}", "host":"{}", "database":"{}"'.format(encrypted_array[0].decode(), encrypted_array[1].decode(), encrypted_array[2].decode(), encrypted_array[3].decode())
text_file = open("db.json", "w")
n = text_file.write("{"+json_content+"}")
text_file.close()