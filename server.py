import socket
s = socket.socket()
print('socket craeted')
s.bind(('localhost',9999))
s.listen(2)
print('waiting for connections')

while True:
    C,addr = s.accept()
    print("connected with",addr)
    name = C.recv(1024).decode()
    C.send(bytes('welcome to bharaths world','utf-8' ))
    C.close()
