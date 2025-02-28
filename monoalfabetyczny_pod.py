def encryption(zwykły):
    kod = ""
    zaszyfrowany = ""
    for char in zwykły:
        distance = ord(char) - ord("a")
        litera_ascii_zaszyfrowana = ord("z") - distance
        kod += chr(litera_ascii_zaszyfrowana)

    return kod

def decode(zaszyfrowany):
    kod = ""
    odszyfrowany = ""
    for char in zaszyfrowany:
        distance = ord("z") - ord("char")
        litera_ascii_odszyfrowana = ord("a") + distance
        kod += chr(litera_ascii_odszyfrowana)
    return kod



def main():
    dane1 = input("Podaj wiadomość do zaszyfrowania: ")
    print(encryption(dane1))
    dane2 = input("Podaj wiadomość do zaszyfrowania: ")
    print(encryption(dane2))


main()
