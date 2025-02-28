import json

def dodaj_produkt(produkty):
    while True:
        nazwa_p = input("Podaj nazwę produktu (Aby wrócić do MENU kliknij ENTER): ")
        if nazwa_p == "":
            return
        try:
            cena = float(input("Podaj cenę produktu: "))
        except ValueError:
            print("Cena musi być liczbą!!")
            continue

        waluta = input("Podaj walutę do jakiej odnosi się cena w zależności od ilości produktu (Np.zł/kg): ")
        if waluta == "" or waluta.isspace():
            print("Musi to być waluta ,która odnosi się do ilości produktu.")
            continue

        try:
            ilość_p = int(input("Podaj ilość produktu: "))
        except ValueError:
            print("Ilość musi być liczbą!!")
            continue

        wartość = input("Podaj wartość ilości, w której dodajesz przedmiot: ")
        if wartość == "" or wartość.isspace():
            print("Wartość opisująca ilość to jednostka, np kg.")
            continue

        while True:
            try:
                identyfikator_p = int(input("Podaj identyfikator produktu, musi być dodatnią liczbą trzycyfrową: "))
            except ValueError:
                print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
                continue

            if identyfikator_p < 100 or identyfikator_p > 999:
                print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
                continue

            if identyfikator_p in produkty:
                print("Ten identyfikator jest już zajęty")
                continue
            break

        produkty[identyfikator_p] = { "nazwa": nazwa_p, "cena": cena, "waluta": waluta, "ilość": ilość_p, "wartość": wartość }
        print("Produkt dodany pomyślnie.")

def dostępne_produkty(produkty):
    print("Dostępne produkty: ")
    for i in produkty.items():
        print(i)


def usuwanie_produktu(produkty):
    while True:
        b = input("Podaj identyfikator produktu, który chcesz usunąć (Aby wrócić do MENU, kliknij ENTER): ")
        if b == "":
            return

        try:
            b = int(b)
        except ValueError:
            print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
            continue

        if b < 100 or b > 999:
            print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
            continue
        break

    if b not in produkty:
        print("Błąd!!! Produkt o takim identyfikatorze nie figuruje w naszym systemie.")
        return

    produkty.pop(b)
    print(f"Produkt o identyfikatorze {b} został usunięty z listy dostępnych produktów.")
    print("Lista produktów po zmianie:")
    for i in produkty.items():
        print(i)

def aktualizacja_ilości(produkty):
    while True:
        try:
            id = int(input("Podaj identyfikator produktu, którego ilość chcesz zaktualizować: "))
        except ValueError:
            print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
            continue

        if id < 100 or id > 999:
            print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
            continue
        break

    if id not in produkty:
        print("Błąd!!!\n Produkt o takim identyfikatorze nie figuruje w naszym systemie.")
        return

    while True:
        try:
            nowa_ilość = int(input("Podaj nową ilość produktu: "))
        except ValueError:
            print("Ilość musi być liczba!")
            continue
        break

    produkty[id]["ilość"] = nowa_ilość
    print(f"Ilość produktu o identyfikatorze {id} została zaktualizowana.")

def sprzedaż(produkty):
    while True:
        while True:
            id = input("Podaj identyfikator produktu, który chcesz zakupić (Aby wrócić do MENU, kliknij ENTER): ")
            if id == "":
                return

            try:
                id = int(id)
            except ValueError:
                print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
                continue

            if id < 100 or id > 999:
                print("Identyfikator musi być dodatnią liczbą trzycyfrową!!")
                continue
            break

        if id not in produkty:
            print("Błąd!!!\n Produkt o takim identyfikatorze nie figuruje w naszym systemie.")
            continue

        ilość_p = produkty[id]["ilość"]
        while True:
            try:
                l = int(input("Podaj ilość produktu jaką chcesz zakupić: "))
            except ValueError:
                print("Ilość musi być liczba!")
                continue

            if l > ilość_p:
                print(f"Nie posiadamy na stanie takiej ilości produktu.\n Ilość tego produktu jaką posiadamy to : {ilość_p}")
                continue
            break

        nowa_ilość = ilość_p - l
        produkty[id]["ilość"] = nowa_ilość
        print("Dziękujemy za zakupy w naszym magazynie i polecamy się na przyszłość.")

def save_dostępne_produkty(produkty):
    with open("magazyn.json", "w", encoding="UTF-8") as f:
          json.dump(produkty, f, ensure_ascii=False)
    print("Stan magazynu został zapisany")

def wczytaj_stan(produkty):
    try:
        with open("magazyn.json","r") as f:
            stan = json.load(f)
            for id in stan:
                produkty[int(id)] = stan[id]
        print("Stan magazynu został wczytany")
        dostępne_produkty(produkty)
    except FileNotFoundError:
        print("Błąd!!! Plik z zapisem stanu magazynu nie istnieje!")

def zakończ():
    print("Do widzenia!")
    exit()

def main():
    produkty = {}

    while True:
        opcje = [
            "Dostępne produkty",
            "Dodaj produkt",
            "Usuń produkt",
            "Aktualizuj ilość",
            "Sprzedaż",
            "Zapisz stan magazynu",
            "Wczytaj stan magazynu",
            "Zakończ"
        ]

        print("Witaj w magazynie!\n *****MENU*****")


        for i in range(len(opcje)):
            print(f"[{i+1}] {opcje[i]}")
        a = input("Wybierz czynność, którą chcesz wykonać: ")

        match a.lower():
            case "dostępne" | "dostępne produkty" | "1":
                dostępne_produkty(produkty)

            case "dodaj produkt" | "dodaj" | "2" | "dodaj produkty":
                dodaj_produkt(produkty)

            case "usuń produkt" | "usuń" | "3" | "usuwanie produktu" | "usuwanie" | "usuń produkty":
                usuwanie_produktu(produkty)

            case "aktualizuj ilość" | "aktualizuj" | "aktualizuj ilosć produktów" | "4":
                aktualizacja_ilości(produkty)

            case "sprzedaż" | "sprzedać" | "5" | "sprzedać produkt" | "sprzedaj produkty" | "sprzedaj":
                sprzedaż(produkty)

            case "zapisz" | "zapisz stan" | "zapisz do pliku" | "6" | "zapisz stan magazynu":
                save_dostępne_produkty(produkty)

            case "wczytaj" | "wczytaj stan" | "wczytaj stan magazynu" | "wczytaj poprzedni stan magazynu" | "importuj" | "7":
                wczytaj_stan(produkty)
            case "zakończ" | "zamknij"| "8":
                zakończ()
            case _:
                print("Nieznana operacja!")


if __name__ == "__main__":
   main()



















