#!/usr/bin/env python

import sys
import requests
from nacl import secret
from nacl.exceptions import CryptoError
from hashlib import sha256
from getpass import getpass

def read_api_token():
    with open("api_key", "rb") as f:
        salt = f.read(secret.SecretBox.KEY_SIZE)
        msg = f.read()
        pwd = sha256()
        pwd.update(getpass("Enter password for API token:").encode('utf-8'))
        pwd.update(salt)
        safe = secret.SecretBox(pwd.digest())
        try:
            return safe.decrypt(msg)
        except (ValueError, CryptoError):
            sys.stderr.write("Cannot decrypt. Wrong api_key file format or wrong password entered.\n\n")
            exit(-1)

try:
    mac = sys.argv[1]
except IndexError:
    sys.stderr.write('Usage: %s AA:BB:CC:DD:EE:FF\n\n' % sys.argv[0])
    exit(-1)

query = 'https://api.macaddress.io/v1?search=%s'
auth_h = { 'X-Authentication-Token': read_api_token()}

r = requests.get(query % mac, headers=auth_h)
if r.status_code != 200:
    sys.stderr.write(r.status_code)
print(r.content.decode())

