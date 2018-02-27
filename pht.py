#!/usr/bin/python

import os
import json


class PersonalHashTracker(dict):
    def __init__(self, filename):
        self.filename = filename
        if os.path.isfile(filename):
            with open(filename) as f:
                # use super here to avoid unnecessary write
                super(PersonalHashTracker, self).update(json.load(f) or {})

    def __setitem__(self, key, value):
        super(PersonalHashTracker, self).__setitem__(key, value)
        with open(self.filename, "w") as f:
            json.dump(self, f)

    def __delitem__(self, key):
        super(PersonalHashTracker, self).__delitem__(key)
        with open(self.filename, "w") as f:
            json.dump(self, f)

    def update(self, d, **kwargs):
        super(PersonalHashTracker, self).update(d, **kwargs)
        with open(self.filename, "w") as f:
            json.dump(self, f)


MENU = """What do you want to do?
a)Add a new IPFS hash
s)Seach stored ha:shes
d)Delete stored hash
q)Quit
>>"""

if __name__ == "__main__":
    hash_store = PersonalHashTracker("/Users/troywilson/testing/pht/hash.json")
    if not hash_store:
        hash_store['hashlist'] = {}

    while True:
        choice = raw_input(MENU)
        if choice == 'a':
            # Add a new hash.
            description = raw_input('Enter hash description: ')
            new_hash_val = raw_input('Enter IPFS hash: ')
            new_url_val = raw_input('Enter URL: ')

            if new_hash_val not in data['hashlist']:
                hash_store['hashlist'][new_hash_val] = {'description': description, 'url': new_url_val}
            else:
                print 'Hash exist!'
        elif choice == 's':
            # Search the current desciptions.
            search_term = raw_input('Enter search term: ')
            descriptions = {v['description']: h for h, v in hash_store['hashlist'].items()}
            print(descriptions.get(search_term, 'Not Found'))
        elif choice == 'd':
            # Search the current descriptions and delete entry.
            del_hash = raw_input('Hash to delete: ')
            del data['hashlist'][del_hash]
            print 'Hash removed'
        else:
            print 'Exiting'
            break
