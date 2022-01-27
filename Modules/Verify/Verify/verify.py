import hashlib
import os
import random

def hash_passwd(passwd, n=32):
    """ Funkcja szyfrująca hasło.

        Args:
            passwd (str): Hasło.
            n (int): Długość szyfru.

        Returns:
            str: _salt.
            str: _hash.
    """
    _salt = os.urandom(n)
    _hash = hashlib.pbkdf2_hmac("sha256", passwd.encode("utf-8"), _salt, 100000)
    return _salt, _hash

