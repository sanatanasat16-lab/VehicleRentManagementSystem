from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__ (self,name,purchase_year,rental_price):
        self.name = name
        self.purchase_year = purchase_year
        self.__rental_price = rental_price

    def display_details(self):
        print(f'{self.name},{self.purchase_year},{self.__rental_price}')
        
    @property
    def rental_price(self):
        return self.__rental_price
    
    @abstractmethod
    def calculate_rent(days):
        pass 

