import hashlib
import secrets
import string


def hash_Password(password):
    hash_pass = hashlib.md5()
    text = password.encode('utf-8')
    hash_pass.update(text)
    return hash_pass.hexdigest()


def generate_passord():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    pw = "".join(secrets.choice(chars) for i in range(10))
    return pw
