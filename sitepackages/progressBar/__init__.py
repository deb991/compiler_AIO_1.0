#!/usr/bin/env python -i
import os
import sys
import socket


print('This is server side script & will define a server at the very begining :[]')

print('Creating socket ~\n')
soc = socket.socket()
print('socket creation successfully: \n')

port = 12345

print('\tNow Binding socket with port number : ')
soc.bind(('', port))

print('Putting server into listen mode : \n')
soc.listen(5)
print('socket is listening :: ')


print('Now putting altogethet & let server communicate with clients :: []\n')
while True:
    print('Establishing connection with Client :: []')
    c, addr = soc.accept()
    print('Client coonnected successfully ::' %(addr))

    c.send(b'Connection success')

    c.close()
    print('Connection closed :: []')
