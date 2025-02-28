import socket

Ip = "127.0.0.1"
Port = 8800
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Ip,Port))
s.listen(2)
while True:
    client,addr = s.recv(1024)
    print(f"Połączono z {addr}")
    mess = "Połączono z serwerem"
    client.send(mess)
    while True:
        a = client.recv(1024)
        print(a)