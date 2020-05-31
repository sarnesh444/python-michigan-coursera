import socket
#socket is like the gateway to communicate with a web service
#initializing socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
#data.pr4e.org-domain name
#80-port number
print("connection succesful")