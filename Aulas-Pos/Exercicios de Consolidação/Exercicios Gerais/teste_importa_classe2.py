from teste_classe2 import Car

my_new_car = Car('Chevrolet', 'Onix', 2025)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.read_odometer()
print()

my_used_car = Car('Chevrolet', 'Onix', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(62500)
my_used_car.read_odometer()
