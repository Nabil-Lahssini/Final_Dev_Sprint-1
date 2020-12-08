import mysql.connector
from cryptography.fernet import Fernet
import json

#load the json file
json_file = open('db.json')
variables = json.load(json_file)
json_file.close()

#read the key to decrypt
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()
f = Fernet(key)

#put the values from the json to an array and decrypting them
my_list = []
for values in variables:
    my_list.append(f.decrypt(variables[values].encode()).decode())


#make the connection with the database using the decrypted value
def connect() :
    cnx = mysql.connector.connect(user=my_list[0], password=my_list[1],
                              host=my_list[2],
                              database=my_list[3])
    return cnx