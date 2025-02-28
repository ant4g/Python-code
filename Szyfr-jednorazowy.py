def encryption(text, key, alfabet):
    kod = ""
    text = text.upper()
    key = key.upper()
    for i in range(len(text)):
        if text[i] in alfabet:
            text_index = alfabet.find(text[i])
            key_index = alfabet.find(key[i % len(key)])
            wynik = text_index + key_index
            kod += alfabet[wynik]
        else:
            kod += text[i]
    return kod

def main():
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dane = input("Podaj wiadomość do zaszyfrowania: ")
    key = input("Podaj klucz szyfrowania: ")
    print("Po zaszyfrowaniu: ")
    print(encryption(dane, key,  alfabet))

main()
