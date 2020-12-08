from cryptography.fernet import Fernet

def load_key():
    return open("key.key","rb").read()


def decrypt(encrypted_key):
    key=load_key()
    f=Fernet(key)
    decrypted_key= f.decrypt(encrypted_key)
    print(decrypted_key.decode())

