def statystyka(kod):
    licznik = {}
    kod = kod.replace(" ", "").upper()
    len_kodu = len(kod)
    for char in kod:
        if char in licznik:
            licznik[char] += 1
        else:
            licznik[char] = 1

    print("Analiza: ")
    for k in licznik:
        print(f"Częstość występowania litery:  {k} to: {(licznik[k] / len_kodu) * 100} %")
    return 0


def main():
    kod = input("Podaj zaszyfrowaną wiadomość do analizy: ")
    statystyka(kod)


main()
