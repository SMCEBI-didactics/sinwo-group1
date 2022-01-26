import hashlib
import os
import random

def hash_passwd(passwd, n=32):
    """ Funkcja szyfrująca hasło

        Parameters:
            passwd String: Hasło
            n int: Długość szyfru

        Returns:
            _salt
            _hash
    """
    _salt = os.urandom(n)
    _hash = hashlib.pbkdf2_hmac("sha256", passwd.encode("utf-8"), _salt, 100000)
    return _salt, _hash

