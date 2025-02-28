import http.server
import socketserver

Port = 8001
IP = '127.0.0.1'
handler = http.server.SimpleHTTPRequestHandler # jest to obsługa żądań dla serwera http
nagłówek = input("Podaj napis do wyświetlenia: ")
with socketserver.TCPServer((IP,Port),handler) as httpd: #jest to instancja serwera, czyli przypisanie wartości na,których będzie dziłał
    with open('index.html','w') as file:
        file.write(f"<html><body><h1>{nagłówek}</h1></body></html>")
    httpd.serve_forever()