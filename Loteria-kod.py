import random

class Lotery():
    def __init__(self):
        self.dane = ['3','5','54','12','80','33','21','9','2','22','45','23','11','37','47','87','77']
        self.a = random.sample(self.dane,4)
    def get_winning_cupon(self):
        print("******* WYNIK LOSOWANIA ********")
        print(f"Zwycięski kupon to: {self.a}.")


    def my_ticket(self):
        self.b = []
        próba = 1
        while self.b != self.a:
            self.b = random.sample(self.dane,4)
            próba += 1
            print(f"Sukces, udało się po {próba} próbach.")
        print(f"Prawdopodobieństwo teoretyczne wygrania w tej loterii znając bazę danych to: {1/próba}")
        print(self.b)



lucky = Lotery()
lucky.my_ticket()
lucky.get_winning_cupon()


