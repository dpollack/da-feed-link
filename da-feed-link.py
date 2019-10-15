import sys
import re
import urllib.request


uname = sys.argv[1]
url = 'https://www.deviantart.com/' + uname + '/gallery/'
html = urllib.request.urlopen(url)
doc = html.read().decode()
parts = doc.split(",")
for each in parts:
    if re.search(r'featured"', each):
        tags  = each.split("<")
for item in tags:
    if re.search(r'featured"', item):
        urlparts = item.split("/")

galleryid = urlparts[5]
feedurl = "http://backend.deviantart.com/rss.xml?q=gallery:" + uname + "/" + galleryid + "&type=deviation"
print (feedurl)
