### 2.2
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)

# size = input('Enter size symbol: ')

# if size == 'S':
#     print('S: Small size')
# elif size == 'M':
#     print('M: Medium size')
# elif size == 'M':
#     print('L: Large size')
# elif size == 'XL':
#     print('XL: Extra large size')
# else:
#     print('Incorrect symbol')

### 2.3
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.

# driving_mode = input('Enter driving mode (A/M/E):')
# distance = int(input('Enter distance in km'))

# if driving_mode == 'A':
#     fuel_consumption = 7 # liters per 100km
# elif driving_mode == 'M':
#     fuel_consumption = 9 # liters per 100km
# elif driving_mode == 'E':
#     fuel_consumption = 6 # liters per 100km
# else:
#     print("Incorect")

# total_consumption = (distance/100)*fuel_consumption
# print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')

###2.4
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   

# number1 = int(input("Enter first number: "))
# number2 = int(input ("Enter second number: "))
# operator = input ("Enter woperator: ")

# if operator == '+':
#     result = number1 + number2
# elif operator == '-':
#     result = number1 - number2 
# elif operator == '*':
#     result = number1*number2
# elif operator == '/':
#     result = number1/number2

# # print result
# print(f'{number1} {operator} {number2} = {result}')

###2.5
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
# month = int(input('Enter month number (1..12): '))

# if month >= 10:
#     quarter = 4
# elif month >=7:
#     quarter = 3
# elif month >=4:
#     quarter = 2
# else:
#     quarter = 1

# print(f'Month {month} is in quarter {quarter}')

### 2.6

# number = int(input("Enter number: "))

# if number < 0:
#     print("negative")
# elif number > 0:
#     print("positive")
# else: 
#     print("Number is 0")

