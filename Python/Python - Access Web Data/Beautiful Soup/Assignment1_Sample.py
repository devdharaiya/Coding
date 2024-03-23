import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts = 0.00
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html', context=ctx).read()
soup = BeautifulSoup(url, 'html.parser')

#Get all Counts
tags = soup('span')
for tag in tags:
    counts = counts + float(tag.contents[0])
print(counts)