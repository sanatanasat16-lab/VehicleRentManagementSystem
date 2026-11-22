from abc import ABC, abstractmethod     

class Vehicle(ABC):                                           # parent class
    def __init__ (self,name,purchase_year,rental_price):
        self.name = name
        self.purchase_year = purchase_year
        self.__rental_price = rental_price

    def display_details(self):                # to display the details of rented vehicle
        print(f'{self.name},{self.purchase_year},{self.__rental_price}')
        
    @property          # property to acess the private variable __rental_price
    def rental_price(self):
        return self.__rental_price
    
    @abstractmethod                        # to calculate rent for some no. of days 
    def calculate_rent(days):
        pass 

