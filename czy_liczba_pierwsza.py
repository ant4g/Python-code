from math import sqrt
from art import *
Art=text2art("Prime Numbers  :)")
print(Art)

def is_prime():
    num = int(input("Wprowadź liczbę do sprawdzenia: "))
    if num < 2:
        print("Nie jest to liczba pierwsza")
        return
    for i in range(2,int(sqrt(num)) + 1):
        if num % i == 0:
            print("Nie jest to liczba pierwsza")
            return
    print("Jest to liczba pierwsza")
while True:
    is_prime()


