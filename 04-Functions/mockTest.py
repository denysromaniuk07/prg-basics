#1 

# def f(n):
#     for char in n:
#         if char not in "01":
#             return False  
#     return 


# print(f("101101"))       # Output: True
# print(f("1311a10100"))   # Output: False

# def f(sentense, letter):
#     count = 0
#     for char in sentense:
#         if char == letter:
#             count+=1
#     return count 


# print(f("You never get a second chance to make a first impression", "e"))


# def f(number, even):
#     number_str = str(number)

#     digits = []

#     for char in number_str:
#         digits.append(int(char))
    
#     sum = 0

#     if even:
#         for digit in digits:
#             if digit %2 == 0:
#                 sum += digit
#     else: 
#         for digit in digits:
#             if digit %2 != 0:
#                 sum += digit
#     return sum

# print(f(3124,True)) 
# print(f(3124,False))


# def power(x ,n):
#     if n == 0:
#         return 1
#     else: 
#         return x * power(x, x-1)

# def sum_natural(n):
#     if n == 1:
#         return 1
#     return n + sum_natural(n - 1)

# print(sum_natural(1)) 


# def factorial(n):

# # 0! = 1, 1! = 1
#     if n==0 or n==1:
#         return 1

# # n! = n * (n-1)!
#     if n > 1:
#         return n * factorial(n-1)

# def f(text):
#     return "*".join(text)

# print(f("Univesity"))
# print(f("University"))  # Виведе: U-n-i-v-e-r-s-i-t-y
# print(f("UE"))          # Виведе: U-E
# print(f("x"))           # Виведе: x
# print(f(""))            # Виведе: ""

# def f(password):
#     return len(password)>=6 and len(set(password)) == len(password)

# print(f("ax15"))
# print(f("book123"))
# print(f("A2water3"))
# print(f("qwerty"))

# def f(n1,n2,n3):
#     small = 0
#     b =0
#     if n1 > n2 > n3:
#         small += n3
#         b +=n1
#     elif n3 > n1>n2:
#         small += n2
#         b+=n3
#     elif n2> n3> n1:
#         small +=n1
#         b +=n2
#     sum = b -small
#     return sum

# print(f(7,4,9))
# print(f(2,12,8))

# def f(n):
#     count = 0
#     num = 1

#     while count<n:
#         num+=1
#         isPrime = True
#         i = 2
#         while i*i <= num:
#             if num%i ==0:
#                 isPrime = False
#                 break
#             i+=1
#         if isPrime:
#             count+=1
#     return num


# print(f(1))
# print(f(5))


# def f(n):
#     digits = str(n)
#     sum = 0
#     for  i in set(digits):
#         if digits.count(i) >1:
#             sum += int(i) * digits.count(i)
#     return sum

# print(f(1027))        
# print(f(230335))     
# print(f(513553007))

def f(palindrome):
    # Залишаємо тільки букви і цифри та перетворюємо на нижній регістр
    cleaned = ''.join(c.lower() for c in palindrome if c.isalnum())
    # Перевіряємо, чи є очищений рядок паліндромом
    return cleaned == cleaned[::-1]

# Приклади виклику функції
print(f("radar"))       # Виведе: True
print(f("12-11-21"))    # Виведе: True
print(f("book"))        # Виведе: False