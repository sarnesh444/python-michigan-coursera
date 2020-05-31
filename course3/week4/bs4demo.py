import urllib.request
from bs4 import BeautifulSoup

url="https://sarnesh444.github.io/COVID-19-Mask-Detector-Web-App/"
#opening and reading url

#read eliminates the need for a loop
html=urllib.request.urlopen(url).read()
#print(html.decode())#gives the entire page
print(html)
#initiating parser
#html-content of the file
#html.parser-used to parse the scraped html file
soup=BeautifulSoup(html,'html.parser')
#tag to look/search for
#returns a list of the searched word here:button
tags=soup('button')
#print(tags)
for tag in tags:
    print(tag.get)
