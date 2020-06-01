import json
import urllib.request

count = 0
sum = 0
url = " http://py4e-data.dr-chuck.net/comments_615387.json"

data = urllib.request.urlopen(url).read()

print(data)

info = json.loads(data)

for i in info['comments']:
    count = count+1
    sum = sum + i['count']
print("Count : ",count)
print("Sum : ",sum)
