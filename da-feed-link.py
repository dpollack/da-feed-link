import sys
import re
import urllib


uname = sys.argv[1]
url = 'https://www.deviantart.com/' + uname + '/gallery/'
html = urllib.urlopen(url)
doc = html.readlines()
for line in doc:
    if re.search(r'galleryId', line):
        parts = line.split(",")
for each in parts:
    if re.search(r'galleryId', each):
        gallerypair  = each.split(":")
galleryid = gallerypair[1].replace('"', '')
feedurl = "http://backend.deviantart.com/rss.xml?q=gallery:" + uname + "/" + galleryid + "&type=deviation"
print feedurl
