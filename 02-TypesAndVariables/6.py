### 6.1
# A program that calculates the number of characters
# of your name, surname and full name
#
# name = 'Anna'   # replace Anna with your name
# surname = 'May' # replace May with your surname
# characters_in_name = len(name)
# print(f'Your name has {characters_in_name} characters')
# print(f'Your surname has  {len(surname)} characters')
# full_name = name + " " + surname
# print(f'Your full name has {len(full_name)}') # with a space between name and surname

### 6.2

# name = 'Denys'
# surname = 'Romaniuk'  
# print(name[0] + surname[0])

### 6.3

###
# A program that prints a university abbreviation
#   
# university = "Krakow University of Economics"
# print(university[0] + university[7] + university[21]) 

### 6.4

# employee = "Mr. John May, born on 1998-02-16"

# name = employee[4:8]          
# surname = employee[9:12]     
# dob = employee[27:]          

# initials = f"{name[0]}{surname[0]}"  

# print(f'Name: {name}')
# print(f'Surname: {surname}')
# print(f'Born: {dob}')
# print(f'Initials: {initials}')

### 6.5

# phone = input('Enter phone number: ')

# if len(phone) == 9 and phone.isdigit():
#     formatted_phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
    
#     print(f"Phone number: {formatted_phone}")
# else:
#     print("Please enter a valid 9-digit phone number.")

### 6.6
# A program to print numerical representations of characters.
#
# print(f'a: {ord('a')}')
# print(f'b: {ord('b')}')
# print(f'z: {ord('z')}')
# print(f'A: {ord('A')}')
# print(f'B: {ord('B')}')
# print(f'Z: {ord('Z')}')
# print(f'1: {ord('1')}')
# print(f'=: {ord('=')}')
# print(f'+: {ord('+')}')
# print(f'€: {ord('€')}')

### 6.7

# A program that prints a numerical representation of each letter of your name.
#
# name = 'Denys'  # Replace 'John' with your name

# print(f'The letter {name[0]} has a code {ord(name[0])}')
# print(f'The letter {name[1]} has a code {ord(name[1])}')
# print(f'The letter {name[2]} has a code {ord(name[2])}')
# print(f'The letter {name[3]} has a code {ord(name[3])}')

### 6.8
# A program that calculates
# how many letters are between two given letters
#
# first = input('Enter first letter: ')
# last = input('Enter last letter: ')

# first_letter_code = ord(first)
# last_letter_code = ord(last)

# number_of_letters = abs(last_letter_code - first_letter_code) - 1

# print(f'Between {first} and {last} is {number_of_letters} letters')

### 6.9
# print(chr(67),chr(111),chr(111),chr(108),chr(88))

### 6.10

# movie = "The Lord of the Rings: The Return of the King"

# print('Number of characters: ', len(movie))

# print('Title in capital letters:', movie.upper())

# print('Title in small letters:', movie.lower())

# count_e = movie.lower().count('e')
# print('Number of times the vowel "e" appears:', count_e)

# index_lord = movie.find("Lord")
# if index_lord != -1:
#     print('The word "Lord" is found at index:', index_lord)
# else:
#     print('The word "Lord" is not found in the title.')

# index_dragon = movie.find("dragon")
# if index_dragon != -1:
#     print('The word "dragon" is found at index:', index_dragon)
# else:
#     print('The word "dragon" is not found in the title.')

