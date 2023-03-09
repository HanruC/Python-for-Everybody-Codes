import collections
collections.Callable = collections.abc.Callable
import urllib
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter URL: ')
# Retrieve all of the anchor tags
pos = int(input('Enter position: ')) - 1  # 18
count = int(input('Enter count: ')) # 7

for i in range(count): # 7 times
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') # choose tag 'a'
    tag_chose = tags[pos].get('href', None) # 18th url
    url = tag_chose # update new tag to the tag chosen on 18th pos
    name = tags[pos].contents[0] # get the name of 18th url
    print(name)
    
