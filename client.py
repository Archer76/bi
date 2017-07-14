import socket
import sys
import time
import base64
from Crypto.Cipher import AES
from Crypto import Random
password = '78f40f2c57eee727a4be179049cecf89'
def encrypt(data, password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    iv = Random.new().read(bs)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = cipher.encrypt(pad(data))
    data = iv + data
    return data

def decrypt(data, password):
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s : s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data  = unpad(cipher.decrypt(data[bs:]))
    return data
'''if __name__ == '__main__':
    asd = raw_input("aaa")
    data = asd
    password = '78f40f2c57eee727a4be179049cecf89'
    encrypt_data = encrypt(data, password)
    encrypt_data = base64.b64encode(encrypt_data)
    print 'encrypt_data:', encrypt_data
'''
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print 'Failed to create socket.Error code: ' + str(msg[0]) + ',Error message : ' + msg[1]
    sys.exit()

print 'Socket created'
remote_ip = raw_input('Enter URL or IP address\n> ')
port = 47071
s.connect((remote_ip,port))
print 'Socket connected to ' + remote_ip
while True:
    nowtime = time.ctime()
    message = raw_input('Enter message here\n>')
    if message == 'exit()':
        sys.exit()
    try:
        s.sendall(base64.b64encode(nowtime[11:19] + ' ' + encrypt(message,password)))
    except socket.error:
        print 'Send failed'
        sys.exit()
