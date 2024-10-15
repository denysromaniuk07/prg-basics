#############       Binary Operations

### 7.1

# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.

# age = int(input('Enter age: '))
# no_tax = age <= 26
# print(f'Exemption from paying taxes: {no_tax}')

### 7.2
# A program that checks whether the password length
# read from the keyboard is correct.
#
# password = input('Enter password: ')
# password_ok = len(password) >= 8
# print(f'Password length is valid: {password_ok}')

### 7.3
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#

# number = int(input('Enter number: '))
# even = number%2==0
# print(f'Number is even: {even}')

### 7.4
# import math

# circumference = float(input('Enter tree circumference in cm: '))
# diameter = circumference / math.pi
# can_cut_down = diameter >= 50

# print(f'Tree can be cut down: {can_cut_down}')

### 7.5

# car_number = input('Enter car registration number: ')
# is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
# print(f'Car is from Krakow: {is_krakow}')


### 7.6

# speed = int(input('Enter vehicle speed (in km/h): '))
# is_correct_speed = 40 <= speed <= 140
# print(f'Is the vehicle speed correct? {is_correct_speed}')

### 7.7

# import random
# random_number = random.randint(5,10)
# print(random_number)

### 7.8

# import random
# dice_roll_1 = random.randint(1, 6)
# dice_roll_2 = random.randint(1, 6)
# dice_roll_3 = random.randint(1, 6)

# total = dice_roll_1 + dice_roll_2 + dice_roll_3
# print(total)

### 7.9

# import random

# dice_roll_1 = random.randint(1, 6)
# is_special_number = dice_roll_1 == 1 or dice_roll_1 == 6
# print(is_special_number)


### 7.10

# import random
# # COMPUTER TURN
# computer = random.randint(1, 6)
# # YOUR TURN
# you = input("Enter: ")
# guesed = you == computer
# print(f'You won: {guesed}')