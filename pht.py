#!/usr/bin/python
# PHT - Personal Hash Tracker
#
import json
import os

hashjson_global = "/Users/troywilson/testing/pht/hash.json"

choice = raw_input("What do you want to do? \n a)Add a new IPFS hash\n s)Seach stored hashes\n d)Delete stored hash\n >>")

if choice == 'a':
    # Add a new hash.
    description = raw_input('Enter hash description: ')
    new_hash_val = raw_input('Enter IPFS hash: ')
    new_url_val = raw_input('Enter URL: ')
    entry = {new_hash_val: {'description': description, 'url': new_url_val}}

    # search existing hash listings here
    if new_hash_val not in data['hashlist']:
    # append JSON file with new entry
        data['hashlist'].update(entry) #must do update since it's a dictionary
        with open(hashjson_global, 'w') as file:
            json.dump(data, file, sort_keys = True, indent = 4, ensure_ascii = False)
        print('IPFS Hash Added.')
        pass
    else:
        print('Hash exist!')
        
elif choice == 's':
    # Search the current desciptions.
    searchTerm = raw_input('Enter search term: ')
    with open(hashjson_global, 'r') as file:
        data = json.load(file)
        hashlist = data['hashlist']
    # build dictionary map and search for description value
    d = {v['description']: h for h, v in hashlist.items()}
    print d.get(searchTerm, 'Not Found')


elif choice == 'd':
    # Search the current descriptions and delete entry.
    del_hash = raw_input('Hash to delete: ')
    with open(hashjson_global, 'r') as file:
        data = json.load(file)
    del data['hashlist'][del_hash]
    with open('hashjson', 'w') as file:
            json.dump(data, file, sort_keys = True, indent = 4, ensure_ascii = False)
    print ('Hash removed')
