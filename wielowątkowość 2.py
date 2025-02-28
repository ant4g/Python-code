import os, random, datetime, time, threading
from subprocess import Popen

class Dźwięki():
    def __init__(self,dz1 = 'notify.wav',dz2 = 'ringout.wav',dz3 = 'chimes.wav', dz4 ='ding.wav',dz5 = 'tada.wav',dz6 = 'Ring05.wav'):

            self.dz1 = input("Podaj dźwięk dla pierwszej potrawy(Jeżeli nie chcesz kliknij Enter): ") or dz1

            self.dz2 = input("Podaj dźwięk dla drugiej potrawy(Jeżeli nie chcesz kliknij Enter): ") or dz2

            self.dz3 = input("Podaj dźwięk dla trzeciej potrawy(Jeżeli nie chcesz kliknij Enter): ") or dz3

            self.dz4 = input("Podaj dźwięk dla czwartej potrawy(Jeżeli nie chcesz kliknij Enter): ") or dz4

            self.dz5 = input("Podaj dźwięk dla piątej potrawy(Jeżeli nie chcesz kliknij Enter): ") or dz5

            self.dz6 = input("Podaj dźwięk dla zakończenia gotowania wszystkich potraw(Jeżeli nie chcesz kliknij Enter): ") or dz6




def kuchnia():
    f = f"Witaj w mojej kuchni!"
    print(f.ljust(6," ") + "\n")
    path = r"\Users\Anton\Desktop\pythonProject\wielowatkowosc\dźwięki"
    print("Zacznijmy od konfiguracji ścieżki dźwiękowej, oto dostępne pliki dźwiękowe: ")
    contents = os.listdir(path)
    print(contents)
    dzwieki = Dźwięki()
    start_time = datetime.datetime.now()
    print(f"Gotowanie rozpoczeło się o: {start_time.strftime('%H:%M')}")


    class Potrawa(threading.Thread):
        def __init__(self, name, time, sound):
            super().__init__()
            self.name = name
            self.time = time
            self.sound = sound
        def run(self):
            self.start_p = datetime.datetime.now()
            print(f"Rozpoczęcie przygotowywania {self.name}")
            time.sleep(self.time)
            print("\n")
            print(f"Zakończenie przygotowywania {self.name} ")
            if os.path.exists(fr"{path}\{self.sound}"):
                Popen(['start', fr"{path}\{self.sound}"], shell=True)
            else:
                print(f"Error: Sound file {self.sound} not found. Using a default sound.")
            self.end_p = datetime.datetime.now()
            self.koniec = self.end_p - self.start_p
            print(f"Przygotowanie {self.name} zajeło: {self.koniec} sekund.")


    do_zrobienia = []
    with open('tasks.txt',encoding='UTF-8') as f:
        print("Lista dań do zrobienia:")
        d = f.readlines()
        for line in d:
            do_zrobienia.append(str(line.rstrip()))



    potrawy = [
        Potrawa(do_zrobienia[0], random.randrange(16,20),dzwieki.dz1),
        Potrawa(do_zrobienia[1], random.randrange(4,6),dzwieki.dz2),
        Potrawa(do_zrobienia[2], random.randrange(11,13),dzwieki.dz3),
        Potrawa(do_zrobienia[3], random.randrange(7,9),dzwieki.dz4),
        Potrawa(do_zrobienia[4], random.randrange(3,6),dzwieki.dz5)
    ]

    for potrawa in potrawy:
        potrawa.start()
    for potrawa in potrawy:
        potrawa.join()

    time.sleep(6)
    print("\n")
    print("Wszystkie dania są gotowe!!")
    path = r"\Users\Anton\Desktop\pythonProject\wielowatkowosc\dźwięki"
    Popen(['start',fr"{path}\{dzwieki.dz6}"], shell=True)
    end_time = datetime.datetime.now()
    print(f"Gotowanie zakończyło się o: {end_time.strftime('%H:%M')}")
    f_time = end_time-start_time
    print(f"Całkowity czas gotowania wyniósł: {f_time} sekund")

    with open('results.txt','w') as f:
        f.write(f"Lista dań: \n")
        for potrawa in potrawy:
            f.write(f"{potrawa.name}\n")
            f.write(f"Czas rozpoczęcia gotowania: {potrawa.start_p.strftime('%H:%M:%S')}\n ")
            f.write(f"Czas zakończenia gotowania: {potrawa.end_p.strftime('%H:%M:%S')}\n ")
            if not os.path.exists(fr"{path}\{potrawa.sound}"):
                f.write(f"Wykryty błąd: Error: Sound file {potrawa.sound} not found. Using a default sound.\n")

    exit()



def main():
    g =f"Witam w programie gotowania kilku potraw na raz."
    h = f"Po zakończeniu gotowania każdej potrawy i zakończeniu gotowania wszystkich usłyszysz dźwięk."
    i = f"Możesz dostosować dźwięk do danej potrawy."
    print(g.ljust(6," "))
    print(h.ljust(6," "))
    print(i.ljust(6," "))
    a = input("Aby rozpocząć gotowanie kliknij Enter: ")
    while True:
        match a.lower():
            case ""|" ":
                kuchnia()
            case _:
                print("Spróbujmy jeszcze raz.")
                a = input("Aby rozpocząć gotowanie kliknij Enter: ")
main()



