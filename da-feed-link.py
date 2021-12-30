import sys
import re
import urllib.request

# when updating need to look for folder-deviations-gallery-XXXXXXXX
uname = sys.argv[1]
url = 'https://www.deviantart.com/' + uname + '/gallery/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
req = urllib.request.Request(url,  headers=headers)
html = urllib.request.urlopen(req)
doc = html.read().decode()
parts = doc.split(",")
for each in parts:
    if re.search(r'folder-deviations-gallery', each):
        tags  = each.split(":")
for item in tags:
    if re.search(r'folder-deviations-gallery', item):
        urlparts = item.split("-")

galleryid = urlparts[3][:-2]
feedurl = "http://backend.deviantart.com/rss.xml?q=gallery:" + uname + "/" + galleryid + "&type=deviation"
print (feedurl)
