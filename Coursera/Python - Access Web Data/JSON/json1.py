import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
} '''

dix = json.loads(data)
print("Name:", dix['name'])
print("Hide:", dix['email']['hide'])