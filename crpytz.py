#!/usr/bin/python2

from getpass import getpass
from pureSalsa20 import Salsa20

# pwgen -sy 32 1

plaintext = bytes(getpass("Type passord, will print ciphertext: "), 'utf-8')
with open('keyfile', 'r') as f:
    key = bytes(f.readline(), 'utf-8')
key = key[:32]
cipher = Salsa20(key=key)
ctext = cipher.encryptBytes(plaintext)
print(ctext)

dec = Salsa20(key=key)
plainagain = dec.decryptBytes(ctext)
if plainagain == plaintext:
    print("OK")
else:
    print("NOPE, plain:", plainagain)
