#class car

class Car:
    make = ''
    name = ''
    year = 0
    miles = 0

    def __init__ (self, make, name, year, miles):
        self.make = make
        self.name = name
        self.year = year
        self.miles = miles
    
    def set_miles(self, miles):
        self.miles = miles
    
    def get_info(self):
        print(f'{self.make} \n {self.name} \n {self.year} \n {self.miles}')

    def get_price(self):
        if self.miles < 5000 :
            print ('예상 가격: 500')
        elif self.miles >= 5000 :
            print ('예상 가격: 1000')

car1 = Car('Tesla', 'Model 3', 2019, 10000)
car1.get_info()
car1.get_price()

car2 = Car('Bugatti', 'Chiron', 2020, 150)
car2.get_info()
car2.get_price()

car3 = Car('Kia', 'Sorento', 2008, 320000)
car3.get_info()
car3.get_price()

