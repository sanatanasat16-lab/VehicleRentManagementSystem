

from Car import Car
from Bike import Bike 

car = Car('Mesarati',2019,60000)
bike = Bike('Unicorn', 2019, 1000)

print('The rent of a Car for 3 days is' ,car.calculate_rent(3))     # the final rental amount of a car which rented for 3 days
print('The rent of a Bike for 3 days is ' ,bike.calculate_rent(3))   # the final rental amount of a bike which rented for 3 days 

car.display_details()    # displaying the details of car 
bike.display_details()      # displaying the details of bike
