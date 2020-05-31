import urllib.request
myurl = urllib.request.Request("http://www.py4inf.com/code/romeo.txt")
resp=urllib.request.urlopen(myurl)
page=resp.read()
for p in page:
    print(p)