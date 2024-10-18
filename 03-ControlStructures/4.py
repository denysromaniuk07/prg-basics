### 4.3
# for i in range(6):
#     print('Practice makes perfect!')

### 4.4
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character)

# university = 'Krakow University of Economics'
# university_expanded = ''

# for char in university:
#     university_expanded = university_expanded + char + ' '


# print(university)
# print(university_expanded)

### 4.5

# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position

# plain_text = 'The early bird catches the worm'
# encrypted_text = ''

# for char in plain_text:
#     if char.isalpha():  
#         char_code = ord(char)
        
#         if char.islower():
#             new_char_code = char_code + 1 if char_code < ord('z') else ord('a')
#         else:
#             new_char_code = char_code + 1 if char_code < ord('Z') else ord('A')
        
#         encrypted_char = chr(new_char_code)
#     else:
#         encrypted_char = char
#     encrypted_text += encrypted_char

# print('Plain text:', plain_text)
# print('Encrypted text:', encrypted_text)

### 4.6

###
# Calculates the sum of integer numbers in the range <1,5>
#
# sum = 0

# for i in range(5,10):
#     sum += i

# print(f'Sum is {sum}')

### 4.7

# Calculates the sum of even numbers in the range <1,10>
#
# sum = 0

# for i in range(1, 10):
#     if not i%2 == 0:
#         continue
#     sum += i

# print(f'Sum of even numbers in the range <1,10> is {sum}')

### 4.8
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for i in range(1,11):
    print(f'1/{i} = {1/i}')