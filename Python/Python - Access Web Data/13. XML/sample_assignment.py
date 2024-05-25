import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
file = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_42.xml', context=ctx).read()
tree = ET.fromstring(file)
lst = tree.findall('.//comment')
for item in lst:
    num = int(item.find('count').text)
    total = total + num
print('Total:', total)
    