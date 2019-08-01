#!/usr/bin/env python

import sys
import requests
from nacl import secret
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
        return safe.decrypt(msg)

query = 'https://api.macaddress.io/v1?search=%s'

auth_h = { 'X-Authentication-Token': read_api_token()}

try:
    mac = sys.argv[1]
except IndexError:
    sys.stderr.write('Usage: %s AA:BB:CC:DD:EE:FF\n\n' % sys.argv[0])
    exit(-1)

r = requests.get(query % mac, headers=auth_h)
if r.status_code != 200:
    print(r.status_code)
print(r.content.decode())

