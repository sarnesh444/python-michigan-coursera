import urllib.request
import re
from bs4 import BeautifulSoup

url = " http://py4e-data.dr-chuck.net/known_by_Uxia.html"
count = int(input('Enter count: '))
position = int(input('Enter position: '))

while count >= 0:
    #retriving name of html file from given url
    name = re.findall('known_by_(.+).html', url)
    print('Retrieving: ' + url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    # Retrieve all the a tags:
    links = soup('a')
    url = links[position - 1].get('href', None)
    count = count - 1

print('Last name found: ',name[0])