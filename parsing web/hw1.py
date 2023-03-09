import collections
collections.Callable = collections.abc.Callable
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1719323.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
sumlist = []
for tag in tags:
    numbers = tag.contents[0]
    sumlist.append(int(numbers))
    count = count + 1
    
print('sum', sum(sumlist))
print(count)
