# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print("File not found")
    quit()
content=fh.read().strip()
content=content.upper()
print(content)