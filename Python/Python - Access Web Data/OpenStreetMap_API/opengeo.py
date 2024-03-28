import urllib.request, urllib.error, urllib.parse
import json, ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter Address:")
    if len(address)<1: break

    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)
    print("Retrieving:", url)
    
    urlh = urllib.request.urlopen(url, context = ctx)
    urlread = urlh.read().decode()
    print("Retrieved:", len(urlread), "characters")

    try:
        data = json.loads(urlread)
    except:
        data = None

    if not data or 'features' not in data:
        print('==== Download error ===')
        print(urlread)
        break

    if len(data['features']) == 0:
        print('==== Object not found ===')
        print(urlread)
        break

    print("lon", data['features'][0]['properties']['lon'])
    print("lat", data['features'][0]['properties']['lat'])
    print("Location:", data['features'][0]['properties']['formatted'])  