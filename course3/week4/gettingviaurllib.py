import urllib.request,urllib.error,urllib.parse

fhand=urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
print("printing html response")
print("#--------------------#")
for line in fhand:
    print(line)
