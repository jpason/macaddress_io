#!/usr/bin/env python

from nacl import secret
from nacl import utils
from hashlib import sha256
from getpass import getpass 

with open("api_key") as f:
    api_key = f.read().rstrip()

salt = utils.random(secret.SecretBox.KEY_SIZE)
pwd = sha256()
pwd.update(getpass("Enter password:"))
pwd.update(salt)
safe = secret.SecretBox(pwd.digest())
encrypted = safe.encrypt(api_key)

with open("api_key", "w") as f:
    f.write(''.join((salt, encrypted)))
