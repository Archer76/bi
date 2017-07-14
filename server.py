import socket
import sys
import time
HOST = ''
PORT = 47071
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket created'
try:
    s.bind((HOST,PORT))
except socket.error,msg:
    print 'Bind failed.Error code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'
s.listen(10)
print 'Socket now listening'
while True:
    nowtime = time.ctime()
    conn, addr = s.accept()
    print 'Connected with '+ addr[0] + ':' + str(addr[1])
    data = conn.recv(1024)
    if data == 'exit()':
        sys.exit()
    else:
        print data
conn.close()
s.close()
