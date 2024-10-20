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

number_p = int(input("Enter number of products: "))
price = int(input("Enter product price: "))

if number_p <= 2:
    amount_to_pay = number_p * price
else:
    amount_to_pay = (2 * price) + ((number_p - 2) * price * 0.75)

print(f"Number of products purchased: {number_p}")
print(f"Product price: {price}")
print(f"Amount to pay: {amount_to_pay}")