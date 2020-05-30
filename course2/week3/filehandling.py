fname=input("Enter file name")
try:
    fhand=open(fname)
except:
    print("File not found, check path")
    quit()
lines=0
characters=0
for i in fhand:
    lines+=1
    characters+=len(i)
print("no of lines in file",lines)
print("no of char in file",characters)
#fhand.read() gives the entire content into var