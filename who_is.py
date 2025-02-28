import socket


def who_is_lookup(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{domain}\r\n".encode())
    respone = s.recv(4096).decode()
    s.close()
    return respone


print(who_is_lookup("google.com"))
