import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
fhand = open('test.txt','w')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter the url- ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
count=0
for tag in tags:
    print(tag.get('href', None))
    fhand.write(tag.get('href',None))
    fhand.write("\n")
    count =count+1
print("total number of <a> tag is ",count)
fhand.close()
