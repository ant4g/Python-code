
from random import choice
słowa = []
a = input("Podaj słowo do wyboru:")
while a != "":
    słowa.append(a)
    a = input("Podaj  kolejne słowo do wyboru:")


wybór = choice(słowa)
hasło = []
print("Oto tajne słowo: " + "_ " * len(wybór))
max_prób = 6

while max_prób >0:
    k = input("Spróbuj zgadnąć pierwszą literę:")
    if len(k) == 1:
        if k in hasło:
            print("Tą liczbę już zgadłeś")
        elif k in wybór:
            print("Zgadłeś!")
            hasło.append(k)
        else:
            print("Nie zgadłeś!")
            max_prób -=1

    odsłonięte_słowo = ""
    for litera in wybór:
        if litera in hasło:
            odsłonięte_słowo += litera
        else:
            odsłonięte_słowo += " _ "
    print("Tajne słowo:", odsłonięte_słowo)
    print("Pozostało prób:",max_prób)



    if k not in wybór:
            if max_prób == 5:
                for i in range(3):
                    print("|")
                print("|"+r"\ "+ "______")
            elif max_prób == 4:
                for i in range(5):
                    print("|")
                print("|"+r"\ "+ "______")
            elif max_prób == 3:
                for i in range(8):
                    print("|")
                print("|"+r"\ "+ "______")
            elif max_prób == 2:
                print("_"*10)
                for i in range(8):
                    print("|")
                print("|"+r"\ "+ "______")
            elif max_prób == 1:
                print("_"*10)
                print("|"+ 9*" "+"|")
                print("|"+ 9*" "+"|")
                for i in range(6):
                    print("|")
                print("|"+r"\ "+ "______")
            elif max_prób == 0:
                print("_"*10)
                print("|"+"/"+ 8*" "+"|")
                print("|"+ 9*" "+"|")
                print("|"+9*" "+"O")
                print("|"+ 8*" "+"/"+"|"+r"\ ")
                print("|"+9*" "+"|")
                print("|"+ 8*" "+"/"+" "+ r"\ ")
                for i in range(4):
                    print("|")
                print("|"+r"\ "+ "______")



if max_prób == 0:
    print("Przegrałeś")
else:
    print("Wygrałeś")















