!ls *.json

#!od -ba testfile2.json

!tr < testfile2.json -d '\000' > testfile2C.json

#import simplejson
import json
json_file_path = "subs.json"

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

import json

def parse(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except ValueError as e:
        print('invalid json: ' + filename)
        return None # or: raise

    
filename = "subs.json"    
parse(filename) 
  

filename = "subs.json"
with open(filename,"w") as outfile:
    json.dump(json_data,outfile)

import json
json.load("subs.json")



