import urllib.request, urllib.error, urllib.parse
import ssl, json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
address = dict()

while True:
    loc = input('Enter Location:')
    if len(loc)<1: break

    address['q'] = loc.strip()
    query = serviceurl + urllib.parse.urlencode(address)
    print("Retrieving:", query)

    try:
        urlh = urllib.request.urlopen(query, context=ctx).read().decode()
        print("Retrieved", len(urlh), 'Characters')

        try:
            parser = json.loads(urlh)
            print("Plus Code:" ,parser['features'][0]['properties']['plus_code'])
            print("Full Address:", parser['features'][0]['properties']['formatted'])
        except:
            parser = None
        
        if not parser or 'features' not in parser:
            print("=== Download Error ===")
            print(urlh)
            break
        
        if len(parser['features']) == 0:
            print('=== Object Not Found ===')
            print(urlh)
            break

    except:
        print("Incorrect Address")