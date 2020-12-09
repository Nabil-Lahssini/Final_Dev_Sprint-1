from cryptography.fernet import Fernet

def load_key():
    return open("key.key","rb").read()


def decrypt(encrypted_key):
    keyt = encrypted_key.encode()
    key=load_key()
    f=Fernet(key)
    decrypted_key= f.decrypt(keyt)
    decrypted = decrypted_key.decode()
    return decrypted
