
from Vehicle import Vehicle    # from Vehicle.py importing Class Vehicle

class Bike(Vehicle):         # child class of Vehicle

    # def __init__ (self,name,purchase_year,rental_price):
    #     super().__init__(name,purchase_year,rental_price)      # since we are not extending child class, super() will not be needed
         
    def calculate_rent(self,days):
        rent = ((self.rental_price * days) + 100)
        return rent     # rental_price is taking from @property
