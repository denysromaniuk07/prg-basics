###7.2

# import calMudle

# number = int(input("Enter mounth: "))
# mounth = calMudle.month(number)
# print(f"The name of month {number} is {mounth}")


###7.3

# def count(text, letter):
#     return text.count(letter)

# text = "You never get a second chance to make a first impression"
# letter = "e"

# count_letter = count(text, letter)
# print(f"The number of letter '{letter}': {count_letter}'")

###7.4 

# import separate_module


# number = int(input("Enter number: "))
# x = 2
# y = 15

# is_in_range = separate_module.separate(number, x, y)

# if is_in_range:
#     print(f"Number {number} in the range <{x}, {y}>: yes")
# else:
#     print(f"Number {number} in the range <{x}, {y}>: no")

###7.5
# import separate_module


# number = "5290312400019022"
# print(f"Number {number} is palindrome: {separate_module.hide(number)}")

###7.6

# def f(binary_number):
#     for char in binary_number:
#         if char == '0' or char == '1':
#             continue
#         else:
#             return False
#     return True    

# print(f("101101"))
# print(f("1311a10100"))

###7.7

# def f(amount):
#     coin5 = 0
#     coin2 = 0
#     coin1 = 0
#     while amount > 0:
#         if amount >= 5:
#             coin5 += 1
#             amount -= 5
#         elif amount >=2:
#             coin2 += 1
#             amount -=2
#         else:
#             coin1 += 1
#             amount -=1
#     amountToPay = coin1 + coin2 + coin5
#     return amountToPay

# print(f(0))

###7.8

# def f(number, even):
#     digit_sum = 0

#     for digit in str(number):
#         digit = int(digit)

#         if even and digit %2==0:
#             digit_sum+=digit
#         elif not even and digit %2 != 0:
#             digit_sum+=digit
#     return digit_sum

# print(f(3124,True))
# print(f(20576,False))

###7.9

# def f(x,y):
#     number = 0
#     if x >=0:
#         return "Error, no negative numbers in range"
#     for digit in range(x,y):
#         if digit < 0 and digit % 2 == 0:
#             number +=1
#     return number
        
# print(f(-7,8))
# print(f(-1,11))

###7.10

# def f(n1,n2,n3):
#     if n1<0 or n2<0 or n3<0:
#         return True
#     else:
#         return False 
    
# print(f(11,6,-4))
# print(f(5,4,14))

###7.11

# def f(n):
    
#     result = ""
#     for i in range(n):
#         result += "*"      
#         if i < n - 1:      
#             result += "/"
    
#     return result

# print(f(4))

###7.12

# def f(n):
#     if n < 0:
#         return "Error"
#     elif n == 0:
#         return 0
#     else:
#         for i in range(n+1):
#             print(i)

# print(f(11))

###7.13

# def f(number1, number2, operator):
#     if operator == "+":
#         return number1 + number2
#     elif operator == "-":
#         return number1 - number2
#     elif operator == "*":
#         return number1 * number2
#     elif operator == "%":
#         return number1 % number2
#     elif operator == "**":
#         return number1 ** number2
#     else:
#         return "Unsupported operator"
    
# print(f(2,3, "+"))
# print(f(2,3, "-"))

###7.14

# def f(detector):
#     count = 0  
    
#     for symbol in detector:
#         if symbol == '+':
#             count += 1 
#         elif symbol == '-' and count > 0:
#             count -= 1  
            
#         if count >= 3:
#             return True
    
#     return False

# print(f("+-+++-+---"))
# print(f("+-+-+-+-"))

###7.15

# def f(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1 
#     else: 
#         return f(n-1) + f(n-2)
        
        
# print(f(3))

# def f(n):
#     if n == 1:
#         return False
#     elif n == 3 or n == 2: 
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     else:
#         return True

# print(f(11))
# print(f(16))


def f(n):
    count = 0  # Лічильник для простих чисел
    num = 1    # Початкове число для перевірки
    
    # Знаходимо n-те просте число
    while count < n:
        num += 1
        is_prime = True
        i = 2
        # Перевіряємо, чи є num простим числом
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        # Якщо число просте, збільшуємо лічильник
        if is_prime:
            count += 1
            
    return num

print(f(2))