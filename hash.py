import hashlib


def hash_Password(password):
    hash_pass = hashlib.md5()
    text = password.encode('utf-8')
    hash_pass.update(text)
    return hash_pass.hexdigest()
