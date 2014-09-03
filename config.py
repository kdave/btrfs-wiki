#!/usr/bin/python

wiki_url='btrfs.wiki.kernel.org'
wiki_proto='https://'
wiki_api='/api.php'
wiki_name='btrfs.wiki'

def wiki_api_url():
    return wiki_proto + wiki_url + wiki_api
