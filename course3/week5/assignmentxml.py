import urllib.request
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_615386.xml"
uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count =0
sum=0
for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x

print("Count : ",count)
print("Sum : ",sum)