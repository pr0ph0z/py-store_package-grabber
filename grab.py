from bs4 import BeautifulSoup
from pprint import pprint
from argparse import ArgumentParser
import re

try:
    # For Python 3.0 and later
    import urllib.request as urllib
    import http.cookiejar as cookielib
except ImportError:
    # Fall back to Python 2's urllib2
    import urllib2 as urllib
    import cookielib

try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

page_count = 1

parser = ArgumentParser()
parser.add_argument("-p", "--page", dest="page",
					help="Jumlah page. Hanya berlaku untuk apk-dl. Selain itu akan diabaikan. Default 1 page")
args = parser.parse_args()

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


site = input("Enter URL: ")

req = urllib.Request(site, headers=hdr)
file = urllib.urlopen(req)
html = file.read()
file.close()

soup = BeautifulSoup(html, 'html.parser')
print ("Scanning site "+site+"\n")

if re.search("apkpure", site):
	soupw = soup.find_all("div", {"class": "category-template-title"})

	for i in soupw:
		print (i.a['href'].split("/")[2])
elif re.search("play.google.com", site):
	soupw = soup.find_all("div", {"data-thin-classes": "card no-rationale square-cover apps small"})

	for i in soupw:
		print (i.div['data-docid'])
elif re.search("apk-dl.com", site):
	if args.page is None:
		soupw = soup.find_all("a", {"class": "title"})

		for i in soupw:
			print(i['href'].split("/")[2])
	else:
		for c in range(1, (int(args.page) + 1)):
			req = urllib.Request(site+"?page="+str(c), headers=hdr)
			file = urllib.urlopen(req)
			html = file.read()
			file.close()

			soup = BeautifulSoup(html, 'html.parser')

			soupw = soup.find_all("a", {"class": "title"})

			for i in soupw:
				print(i['href'].split("/")[2])
elif re.search("apkmonk.com", site):
	soupw = soup.find_all("div", {"class": "col l7 s7 offset-l1 offset-s1 m7 offset-m1"})

	for i in soupw:
		print(i.p.a['href'].split("/")[2])
elif re.search("downloadatoz.com", site):
	soupw = soup.find_all("div", {"class": "s-app-block"})

	for i in soupw:
		print (i.a['href'].encode('ascii','ignore').split("/")[0])
else:
	print("Sitelo ga support bos")