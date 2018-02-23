#!/usr/bin/python
# PHT - Personal Hash Tracker
#
import json
import os

data = []
if os.stat("hash.json").st_size != 0 :
    file = open('hash.json', 'r')
    data = json.load(file)
   # print(data)

choice = raw_input("What do you want to do? \n a)Add a new IPFS hash\n s)Seach stored hashes\n  >>")

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
        with open('hash.json', 'w') as file:
            json.dump(data, file, sort_keys = True, indent = 4, ensure_ascii = False)
        print('IPFS Hash Added.')
        pass
    else:
        print('Hash exist!')
        
elif choice == 's':
    # Search the current desciptions.
    searchTerm = raw_input('Enter search term: ')
    with open('hash.json', 'r') as file:
        data = json.load(file)
    
    # Works
    for key, entry in data['hashlist'].iteritems():
      #  print key, entry['description'] # works
      #  print entry['description'] # works

        if searchTerm in entry['description'] == True:
            print key
        else:
            print "not found"
            
        #if searchTerm in entry(data['description']) == True:
        #    print key

        
#    if searchTerm in data['hashlist']:
#        print ('Found Hash!')
#        print data['hashlist']
#    else:
#        print ('No hash found!')


    # OLD Search working 
#    sglobal = 0
#    for x in data["hashlist"]:
#        if data["hashlist"][sglobal]["description"] == searchTerm:
#            hash = data["hashlist"][sglobal]["ipfsHash"]
#            print "Hash Requested:", hash
#            break
#        else:
#            sglobal += 1


# Notes: How JSON is readable            
   
   # Show Hashes working !
#    print data["hashlist"][0]["ipfsHash"]
#    print data["hashlist"][1]["ipfsHash"]
#    print data["hashlist"][2]["ipfsHash"]
#    etc...
     
   # Show Descriptions working !
#    print data["hashlist"][0]["description"]
#    print data["hashlist"][1]["description"]
#    print data["hashlist"][2]["description"]
#    etc...        
    


    
        
