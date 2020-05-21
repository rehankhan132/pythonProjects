from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        print(e)
    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be completed.")
else:
    print(title)
