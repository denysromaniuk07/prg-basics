### 3.2

###
# Checking login and password
#
# login = 'joe'
# password = 'abcd'
# entered_login = input('Login: ')
# entered_password = input('Password: ')
# if login == entered_login and password == entered_password :
#     print('You are logged in')
# else:
#     print('Incorrect login or password!!')

### 3.3

###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.

# age = int(input('Enter your age: '))

# if age < 18 or age > 65 :
#     print("You have discount")
# else:
#     print("The discount is unavailable for you")

### 3.4
# Checks whether at least one number entered
# from the keyboard is not negative

# x = int(input('Enter first number: '))
# y = int(input('Enter second number: '))

# if not x < 0 or y < 0 :
#     print(f'At least one of the numbers {x} and {y} is not negative')

### 3.5

# Calculates the number of days in a month

# month = int(input('Enter month number (1..12)'))

# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
#     days = 31 ## months with 31 days
# elif month==4 or month==6 or month==9 or month==11:
#     days = 30 ## months with 30 days
# elif month == 2:
#     days = 28
# else:
#     days = 0 

# print(f'Month {month} has {days} days.')

### 3.6

###
# Checks if the given day number of the month is correct

# month = int(input('Enter month number (1..12): '))
# day = int(input('Enter the day number of the month: '))
# day_ok = False

# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     if day >=1 and day <= 31:
#         day_ok = True
# elif month== 4 or month==6 or month==9 or month==11:
#     if day >=1 and day <= 30:
#         day_ok = True
# elif month == 2:
#     if   day >=1 and day<= 28:
#         day_ok = True

# message = f'Day {day} for the month {month}'
# if day_ok:
#     print(f'{message} is correct')
# else:
#     print(f'{message} is uncorrect')