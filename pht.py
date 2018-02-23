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

choice = raw_input("What do you want to do? \n a)Add a new IPFS hash\n s)Seach stored hashes\n d)Delete stored hash - not working\n >>")

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
        hashlist = data['hashlist']
        #print hashlist
        #print searchTerm
        
    # Not working yet
    def search(values, searchFor):
        for k in values:
            for v in values[k]:
                if searchFor in v:
                    return k
            return None

#Checking if string 'Mary' exists in dictionary value
    print search(hashlist, searchTerm) #prints firstName





    
#    def search(hashlist, lookup):
#        for key, value in hashlist.iteritems():
#            for v in value:
#                if lookup in v:
#                    print key
#                    
#    print search(hashlist, 'searchTerm')


                
    #  print key, entry['description'] # works
      #  print entry['description'] # works

     #   if searchTerm in entry['description'] == True:
     #       print key
     #   else:
     #       print "not found"
            
        #if searchTerm in entry(data['description']) == True:
        #    print key

        
#    if searchTerm in data['hashlist']:
#        print ('Found Hash!')
#        print data['hashlist']
#    else:
#        print ('No hash found!')
    
