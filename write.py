#!/usr/bin/python
#
import json

data = {
'hashlist': {
    'QmVZATT8jWoCsNKzy2VruZEt6ncQM3kwBrGXBjuKfifvrE': {
        'description': 'Knox Video',
        'url': ''
    },
         
    'QmVqpEomPZBSWNVmHJEgQ8dU8cpNezxZHG2oc3xQi61P2n': {
        'description': 'Cat Photo',
        'url': ''
    },
    'QmYdWbMy8wyVCmq65R4CdFqWGYnPA7V12bX7hf2zxv64AG': {
        'description': 'labwork.co',
        'url': ''
    }
}
}

with open('/Users/troywilson/testing/pht/hash.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
