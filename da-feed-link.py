import sys
import re
import urllib


uname = sys.argv[1]
url = 'https://www.deviantart.com/' + uname + '/gallery/'
html = urllib.urlopen(url)
doc = html.readlines()
for line in doc:
    if re.search(r'featured"', line):
        parts = line.split(",")
for each in parts:
    if re.search(r'featured"', each):
        tags  = each.split("<")
for item in tags:
    if re.search(r'featured"', item):
        urlparts = item.split("/")

galleryid = urlparts[5]
feedurl = "http://backend.deviantart.com/rss.xml?q=gallery:" + uname + "/" + galleryid + "&type=deviation"
print feedurl
