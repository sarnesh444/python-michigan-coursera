import socket
#socket is like the gateway to communicate with a web service
#initializing socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))
#data.pr4e.org-domain name
#80-port number
cmd="GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n".encode()
#encode converts to UTF-8
#sending get request
mysock.send(cmd)

while(True):
    data=mysock.recv(512) #512-no of char to be retrieved
    if(len(data)<1):
        break
    print(data)
mysock.close()

