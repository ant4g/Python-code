class User():
    def __init__(self,first_name,last_name,age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def greet_user(self):
        print(f"Witaj {self.first.title()} {self.last.title()}")
        print("Oto twój profil użytkownika:")
    def describe_user(self):
        print(f"Imię użytkownika to : {self.first.title()}")
        print(f"Nazwisko użytkownika: {self.last.title()}")
        print(f"Wiek użytkownika to {self.age.title()} lata")

class Admin(User):

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privilages = Privilages()
class Privilages():
    def __init__(self):
        self.privilages = [" dodać post"," usuwać innych członków"," usunąć post"," zbanować użytkownika"]
    def show_privilages(self):
        print("Oto twoje uprawnienia:")
        print("Możesz:")
        for i in self.privilages:
            print(i)

użytkownik_info2 = Admin('Karolina','Bilewiczówna','60')
użytkownik_info2.greet_user()
użytkownik_info2.describe_user()
użytkownik_info2.privilages.show_privilages()
