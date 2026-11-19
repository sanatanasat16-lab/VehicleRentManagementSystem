

from Car import Car
from Bike import Bike 

car = Car('Mesarati',2019,60000)
bike = Bike('Unicorn', 2019, 1000)

print('The rent is ' ,car.calculate_rent())
print('The rent is ' ,bike.calculate_rent())
