
from Vehicle import Vehicle

class Car(Vehicle):      # child class of Vehicle

    # def __init__ (self,name,purchase_year,rental_price):     
    #     super().__init__(name,purchase_year,rental_price)
    
    def calculate_rent(self,days):
         rent = ((self.rental_price * days)+ 500)       # rental_price is taking from @property
         return rent
    