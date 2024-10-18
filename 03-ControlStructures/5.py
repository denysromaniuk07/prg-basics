### 5.3
# Prints a greeting
#
# name = ''

# while name == '':
#     name = input('Enter your name: ')

# print(f'Hello {name}')

### 5.4
# A simple number guessing game

# import random

# # Randomly chosen number to be guessed from 1 to 100
# number_to_guess = random.randint(1, 100)
# user_guess = 0

# print("Guess the number between 1 and 100!")

# while user_guess != number_to_guess:
#     user_guess = int(input("Enter your guess: "))

#     if user_guess < number_to_guess:
#         print("Too low! Try again.")
#     elif user_guess > number_to_guess:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")

### 5.5
# Sums numbers entered by user

# total_sum = 0

# while True:
#     number = int(input("Enter a number (0 to stop): "))
    
#     if number == 0:
#         break  # Exit the loop when 0 is entered
#     total_sum += number

# print(f"The total sum of the numbers is: {total_sum}")

### 5.6

# N = 10
# sum_even = sum(i for i in range(1, N + 1) if i % 2 == 0)

# print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

### 5.7 it is timer.py

### 5.8 it is atm.py