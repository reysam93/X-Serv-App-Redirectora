#!/usr/bin/python


import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 9999))
mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        url = str(random.randrange(10000))
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 300 Not Found\r\n\r\n<html><body>" + 
                        "Rediderecting<meta http-equiv='refresh' content='3;" +
                        "URL=" + url + "'></p>" + "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
