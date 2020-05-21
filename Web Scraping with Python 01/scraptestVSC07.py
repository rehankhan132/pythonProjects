from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'html.parser')

""" children = bsObj.find("table",{"id":"giftList"}).children
for child in children:
    print(child) """
""" descendants = bsObj.find("table",{"id":"giftList"}).descendants
for child in descendants:
    print(child) """
""" siblings = bsObj.find("table",{"id":"giftList"}).tr.next_siblings
for sibling in siblings:
    print(sibling) """
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())