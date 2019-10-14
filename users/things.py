import urllib3
import urllib.request
import re
from urllib3 import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

#http = urllib3.PoolManager()
#data = urllib.request.urlopen('https://api.thingspeak.com/update?api_key=AF2HBXIDNGLXGT3B&field1='+str(1200))
#print(data)
class retrive():
    data_read = urllib.request.urlopen('https://api.thingspeak.com/channels/866457/feeds.json?api_key=ORN9IAZY7TR3K55V&results=2')
    #print(data_read.read())
    select = repr(data_read.read())
    #select = select[384:388]
    #select = select[400:405]
    select = select[300:]
    #print(select)
    #return select
    pick = re.search('field1":"(.+?)",',select)
    #if pick:
     #   print(pick.group(1));

    print(str(pick)[48:51])



