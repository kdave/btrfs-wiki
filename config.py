#!/usr/bin/python2

from pureSalsa20 import Salsa20
import os

wiki_url='btrfs.wiki.kernel.org'
wiki_proto='https://'
wiki_api='/api.php'
wiki_name='btrfs.wiki'

def wiki_api_url():
    return wiki_proto + wiki_url + wiki_api

def readpassword():
    if not os.path.exists('keyfile'):
        return False
    f = open('keyfile')
    key = f.readline()
    f.close()
    key = key[:32]
    cipher = Salsa20(key=key)
    password = cipher.decryptBytes(encryptedpass)
    return password
