import urllib.request
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_615384.html'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,'html.parser')

# Retrieve all the span tags:
spans = soup('span')

# Calculate a sum of all the numbers in the span tags:
sum = 0
for span in spans:
    sum = sum + int(span.contents[0])
print(sum)