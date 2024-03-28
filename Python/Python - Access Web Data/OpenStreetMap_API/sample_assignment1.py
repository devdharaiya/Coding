import urllib.request, urllib.error, urllib.parse
import json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

summation = 0

while True:
    prompt = input("Enter URL:")
    if len(prompt) > 1 : break

data = urllib.request.urlopen(prompt, context = ctx).read()
parser = json.loads(data)
print(len(parser))  

