##########          Practice Makes Perfect        

### 8.1  read something

### 8.2

# import math

# # Calculation of circle area and circumference

# r = float(input('Enter the radius of the circle: '))
# pi = math.pi

# area = pi * r ** 2
# circumference = 2 * pi * r

# print(f'For a circle with radius {r}:')
# print(f'Circumference = {circumference}')
# print(f'Area = {area}')

### 8.3
# A program that reads temperature in degrees Celsius from the keyboard.
# The program converts the Celsius temperature to Kelvin and Fahrenheit
# and then prints the results.

# celsius = float(input('Enter temperature in degrees Celsius: '))
# kelvin = celsius + 273.15
# fahrenheit = (celsius * 9/5) + 32

# print(f'Temperature in Kelvin: {kelvin} K')
# print(f'Temperature in Fahrenheit: {fahrenheit} °F')

### 8.4

# cm = 170
# # 1 foot = 30.48 cm
# # 1 inch = 2.54 cm
# feet = cm // 30.48  
# remaining_cm = cm % 30.48  
# inches = remaining_cm / 2.54  
# print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {inches:.1f} inches')

### 8.5

# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.

# swift = input('Enter SWIFT code: ')
# country_code = swift[4:6]
# bank_code = swift[0:4]
# print(f'Bank Code: {bank_code}')
# print(f'Country Code: {country_code}')

### 8.6

# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.

# distance = int(input('Enter distance in km: '))
# fuel_price = float(input('Enter fuel price per liter: '))
# fuel_consumption = float(input('Enter fuel consuption per 100km: '))
# total_fuel_consumption = (distance/100)*fuel_consumption
# total_cost = total_fuel_consumption*fuel_price
# print(f'Total fuel consumption: {total_fuel_consumption}')
# print(f"Total cost: {total_cost}")

### 8.7

# A program that reads an integer number from the keyboard
# and prints that value as a binary and hexadecimal number.

decimal_number = int(input('Enter an integer: '))

binary_number = bin(decimal_number) 
hexadecimal_number = hex(decimal_number)  

print(f'Decimal: {decimal_number}')
print(f'Binary: {binary_number}') 
print(f'Hexadecimal: {hexadecimal_number}')
