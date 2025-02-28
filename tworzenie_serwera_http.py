import moduł_urllib_pobieranie_zawartości
import socketserver
import http.server
IP = input("Podaj adres IP serwera: ")
Port = int(input("Podaj numer portu: "))


handler = http.server.SimpleHTTPRequestHandler


text = input("Wprowadź treść. która zostanie wyświetlona na stronie: ")
with open('index.html','w') as file:
    file.write(f"<html><body><h1>{text}</h1></body></html>")

httpd = socketserver.TCPServer((IP, Port), handler)

print(f"Serwer HTTP uruchomiony na http://{IP}:{Port}/")
httpd.serve_forever()