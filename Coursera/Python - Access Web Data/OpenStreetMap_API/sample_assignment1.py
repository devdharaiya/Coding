import urllib.request, urllib.error, urllib.parse
import json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sums = 0

while True:
    url = input("Enter URL:")
    if len(url)<1: break

    try:
        data = urllib.request.urlopen(url).read()
        parser = json.loads(data)['comments']
        for item in parser:
            item = int(item['count'])
            sums = sums + item
        print("Sum of Comments:", sums)
    except:
        parser = None
        try:
            if not parser or ['comments'] not in parser:
                print("=== Download Error ===")
        except:    
            if len(parser['comments']) == 0:
                print('=== Object Not Found ===')
        

