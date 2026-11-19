
from Vehicle import Vehicle

class Car(Vehicle):

    # def __init__ (self,name,purchase_year,rental_price):
    #     super().__init__(name,purchase_year,rental_price)
    
    def calculate_rent(self):
         rent = (self.rental_price + self.rental_price * 3)       # rental_price is taking from @property
         return rent
    