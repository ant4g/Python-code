from random import randrange

class Die():
    def Roll_die(self):
        for i in range(10):
            self.dice_throw = randrange(1 , 21)
            print(self.dice_throw)
próba1 = Die()
próba1.Roll_die()


