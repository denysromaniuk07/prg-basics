### 6.3 
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
# light_switch1 = False # False - switch off, True - switch on
# light_switch2 = True
# bulbs_on = 0
# if light_switch1:
#     bulbs_on += 1
# if light_switch2:
#     bulbs_on +=2
# print(bulbs_on)

### 6.4
# Password validator
# New password is at least 12 characters long
#
# new_password = input('Enter new password: ')
# if len(new_password) < 12:
#    print('Password too short (min. 12 chars)') 

### 6.5
# Program that simulates the operation of an electronic thermometer.
#
# temperature = 32
# if temperature > 35:
#     print("It is extermely hot")
# elif temperature > 30:
#     print("It is hot")
# elif temperature >15:
#     print("It is warm")
# elif temperature > 0:
#     print("Warning, frost!")

### 6.6

# parking_hours = int(input("Enter hours of parking: "))

# if parking_hours >= 1 and parking_hours <= 2:
#     print("Your fee is 5PLN")
# elif parking_hours >=3 and parking_hours <= 6:
#     print("Your fee is 15PLN")
# elif parking_hours >=6:
#     print("Your fee is 20PLN")
 
### 6.7 

# age = int(input("Enter hours of parking: "))

# if age <= 13:
#     print("Your group is child")
# elif age > 13 and age <= 19:
#     print("Your group is teen")
# elif age >= 20 and age <= 64:
#     print("Your group is adult")

### 6.9 

# name = input("Enter name: ")

# if name.endswith('a'):
#     print(f"{name} -- Polish famale name")

### 6.10

# human_years = float(input("Enter the dog's age in human years: "))

# if human_years <= 2:
#     dog_years = human_years * 10.5
# else:
#     dog_years = (2 * 10.5) + (human_years - 2) * 4

# print(f"The dog's age in dog's years is {dog_years} years.")

### 6.11 

# price = int(input("Enter previous price: "))
# curent_price = int(input("Enter present price: "))

# percent = ((price - curent_price) / price) * 100

# print(f"Current product price: ")
# print(f"Previous product price: ")

# if percent >= 10:
#     print(f"Buy product!!!")
#     print(f"Product price reduced by: {percent}%")
# else: 
#     print("Don't buy")

### 6.12

# number_p = int(input("Enter number of products: "))
# price = int(input("Enter product price: "))

# if number_p <= 2:
#     amount_to_pay = number_p * price
# else:
#     amount_to_pay = (2 * price) + ((number_p - 2) * price * 0.75)

# print(f"Number of products purchased: {number_p}")
# print(f"Product price: {price}")
# print(f"Amount to pay: {amount_to_pay}")

### 6.13

# car_speed = int(input("Enter speed: "))
# speed_limit_min = 40
# speed_limit_max = 140

# if car_speed <40 or car_speed > 140:
#     print("Warning: invalid car speed!!")
# else: 
#     print("Valid spped")

### 6.14

# facebook = True
# twiter = False
# instagram = True

# if (facebook + twiter + instagram) >= 2:
#     print("You are good influencer!")

### 6.15

# number = input("Enter EAN-13 article number: ")
# if len(number) == 13 and number.isdigit():
#     print("Article number is correct")

#     if number.startswith("590"):
#         print("Article manufactured in Poland")
# else: 
#     print("Article number is uncorrect")

### 6.16

# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
# total_washing_time = 0

# program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').lower()
# extra_rinse = input('Extra rinse? (y/n): ').lower()
# extra_spin = input('Extra spin? (y/n): ').lower()

# if program == 'j':
#     total_washing_time = 40
# elif program == 'u':
#     total_washing_time = 70
# elif program == 's':
#     total_washing_time = 20
# else:
#     print("Invalid program selected")

# if extra_rinse == 'y':
#     total_washing_time += 15

# if extra_spin == 'y':
#     total_washing_time += 9

# if total_washing_time > 0:
#     print(f"Total washing time: {total_washing_time} minutes")
# else:
#     print("Please select a valid washing program")

### 6.17

# hour24 = input("Enter hour in 24-hours format: ")

# hours, minutes = map(int, hour24.split(':'))

# if hours >= 12:
#     period = "pm"
#     if hours > 12:
#         hours = hours - 12
#     else: 
#         hours = 12
# else:
#     period = 'am'
#     if hours == 0:
#         hours = 12
#     else: hours

# print(f"Time in 12-hour format: {hours}:{minutes}{period}")

### 6.18

# x = 5
# y = 2

# if x > 0 and y > 0:
#     print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
# elif x < 0 and y > 0:
#     print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
# elif x < 0 and y < 0:
#     print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
# elif x > 0 and y < 0:
#     print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
# elif x == 0 and y != 0:
#     print(f"Point P({x},{y}) is on the Y-axis")
# elif x != 0 and y == 0:
#     print(f"Point P({x},{y}) is on the X-axis")
# else:
#     print(f"Point P({x},{y}) is at the origin (0,0) of the coordinate system")

### 6.19

# Print the survey
# print("SURVEY")

# interest_cs = input("Are you interested in computer science? (y/n): ").lower() == 'y'
# play_games = input("Do you like playing computer games? (y/n): ").lower() == 'n'
# instagram_account = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

# print("\nSURVEY RESULTS")
# print(f"Interested in computer science: {'Yes' if interest_cs else 'No'}")
# print(f"Playing computer games: {'No' if play_games else 'Yes'}")
# print(f"Has an Instagram account: {'Yes' if instagram_account else 'No'}")

### 6.20

# decimal_number = int(input("Enter decimal number: "))
# binary_num = []

# n = decimal_number
# while n > 0:
#     remainder = n % 2
#     binary_num.append(remainder)
#     n = n // 2

# binary_num.reverse()
# binary_str = ''.join(map(str, binary_num))

# print(f"{decimal_number}(10) = {binary_str}(2)")

### 6.21

# amount = int(input("Enter the amount in PLN: "))

# coin5 = 0
# coin2 = 0
# coin1 = 0

# while amount > 0:
#     if amount >= 5:
#         coin5 += 1
#         amount -= 5
#     elif amount >=2:
#         coin2 += 1
#         amount -=2
#     else:
#         coin1 += 1
#         amount -=1

# print(f"The amount of PLN {amount} in coins")
# print(f"5 PLN coins: {coin5}")
# print(f"2 PLN coins: {coin2}")
# print(f"5 PLN coins: {coin1}")

### 6.22

# for number in range(1,31):
#     if number % 3 == 0 and number % 5==0:
#         print("Bingo", end=" ")
#     elif number % 3 == 0:
#         print("THREE", end= " ")
#     elif number % 5 == 0:
#         print("FIVE", end=" ")
#     else: 
#         print(number, end=" ")

### 6.23

# number = int(input("Enter number: "))

# for i in range (1,10):
#     m = number * i
#     print(f"{number} x {i} = {m}")

### 6.24
# s=""

# for i in range(1,6):
#     if i>=1 and i<=5:
#         s+="*"
#         print(s)
# for i in range(4,0,-1):
#     s="*"*i
#     print(s)
      
### 6.25

# for i in range (1,10):
#     for j in range(i):
#         print(i, end="")
#     print()

### 6.26

# pin = '0805'
# mistake =0

# while mistake <3:
#     user = input("Enter pin code: ")
#     if pin == user:
#         print("Correct")
#     else:
#         print("Incorrect...")
#         mistake= mistake + 1
# print("Sorry, your payment card has been blocked.")

### 6.27
# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f'{i+j}',end=' ')
#     print()
# print()  
# i = 6
# while i > -1:
#     j = 1
#     while j < 4:
#         print(f'{i+j}', end=' ')
#         j += 1
#     print()
#     i -= 3

### 6.28

# n_terms = 20
# n1, n2 = 0, 1
# count = 0

# print("Fibonacci sequence:")
# while count < n_terms:
#     print(n1, end=' ')
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1
# print()

### 6.29

# number = int(input("Enter number: "))
# prime = True
# if number <= 1:
#     prime = False
# elif number == 2 or number == 3:
#     prime = True
# else:
#     for i in range (2,3):
#         if number % i == 0:
#             prime = False
        
# print(prime)

### 6.30

# for i in range (7):
#     for j in range(7):
#         print(i+1+j*7, end=" ")
#     print()

### 6.31

# import random

# for i in range(20):
#     a = random.randint(5,11)
#     print(a)

