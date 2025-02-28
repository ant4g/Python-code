import socket

IP = "127.0.0.1"
Port = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IP,Port))

w = s.recv(1024)
print(f"Wiadomość z serwera: {w}")
while True:
    r = input("Podaj wiadomość do przesłania na serwer")
    s.send(r.encode())