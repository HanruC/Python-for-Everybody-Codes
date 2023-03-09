import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    url = input('enter location: ')
    print('retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    lst =[]
    for each in info['comments']:
        number = each['count']
        lst.append(int(number))
    print(sum(lst))
        
        
    
    

    
    
    
