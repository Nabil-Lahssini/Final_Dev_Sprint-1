import secrets

def checkFile():
    text_file = open("tk", "r")
    lines = text_file.readlines()
    text_file.close()
    return lines

def appendFile(token):
    file_object = open('tk', 'a')
    file_object.write(token)
    file_object.close()
 
def generateId():
    lines = checkFile()
    token = secrets.token_hex(8)
    tokend = token + '\n'
    while tokend in lines:
        token = secrets.token_hex(8)
        tokend = token + '\n'
    appendFile(tokend)
    return token
generateId()