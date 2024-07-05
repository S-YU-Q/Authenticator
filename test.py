import hashlib
import os


def hash_password(pwd):
    pwd = pwd.encode('utf-8')
    hashed_pwd = hashlib.sha256(pwd).hexdigest()
    return hashed_pwd

a = 'yumnondi'
b = hash_password(a)
print(b)