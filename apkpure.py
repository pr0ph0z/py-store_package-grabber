from bs4 import BeautifulSoup
import urllib2, cookielib

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

site = raw_input("Enter APKPure URL: ")

req = urllib2.Request(site, headers=hdr)
apkpureFile = urllib2.urlopen(req)
apkpureHtml = apkpureFile.read()
apkpureFile.close()

soup = BeautifulSoup(apkpureHtml, 'html.parser')
print "Scanning site "+site+"\n"
soupw = soup.find_all("div", {"class": "category-template-title"})
for i in soupw:
	print i.a['href'].split("/")[3]
