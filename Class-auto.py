class Auto():
    def __init__(self,car_brand,car_model,production_year):
        self.brand = car_brand
        self.model = car_model
        self.year = production_year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.brand} {self.model} {self.year}"
        return long_name.title()
    def update_odometer(self,new_mileage):
        if new_mileage >= self.odometer_reading:
            self.odometer_reading = new_mileage
            print(f"Przebieg tego auta wynosi: {self.odometer_reading} km ")
        else:
            print("Nie wolno cofać licznika samochodu")
    def increment_odometer(self,kilomiters):
        self.odometer_reading += kilomiters
        print(f"Aktualny przebieg auta wynosi: {self.odometer_reading}")
car_info = Auto('Toyota', ' Prius','2023')
print(car_info.get_descriptive_name())
car_info.update_odometer(20220)
car_info.increment_odometer(2300)

class Battery():
    def __init__(self, battery_size = 100):
        self.range =600
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"Bateria w tym samochodzie ma pojemność: {self.battery_size}, "
              f"i pozwala na przejechanie {self.range} km")
    def get_range(self):
        if self.battery_size == 75:
            range = 400
        elif self.battery_size == 100:
            range = 600
        print(f"Zasięg na w pełni naładowanym akumulatorze wynosi: {range} km")
class ElectricCar(Auto):

     def __init__(self,car_brand,car_model,production_year):
         super().__init__(car_brand,car_model,production_year)
         self.battery = Battery()

my_tesla = ElectricCar("Tesla", "model Y", "2023")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()







