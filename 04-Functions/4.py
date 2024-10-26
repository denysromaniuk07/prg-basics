###4.3
# Calculates the area of a triangle based on the lengths
# import math

# # Function to calculate the area of a triangle using Heron's formula
# def triangle_area(a, b, c):
#     s = (a + b + c) / 2  # semi-perimeter
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return area

# a1 = int(input("Enter first number: "))
# b1 = int(input("Enter second number: "))
# c1 = int(input("Enter three numbers: "))
# area1 = triangle_area(a1, b1, c1)
# print(f'The area of a triangle with sides {a1}, {b1}, {c1} is {area1}')

###4.4

# def main():
#     any_number = int(input('Enter integer number: '))
#     result = sumDigits(any_number)
#     print(f'The sum of the digits in the number {any_number} is {result}')

# def sumDigits(number):
#     number = abs(number)
#     digit= str(number)
#     count = 0
#     for i in digit:
#         count+=int(i)
#     return count
    
# if __name__ == "__main__":
#     main()

###4.5
# Calculates the final grade for a test based
# on the number of points obtained
#
# def pts_to_grade(points):
#     grade = ''
#     if points >= 18:
#         grade = 'Excellent'
#     elif points >=14:
#         grade = 'Good'
#     elif points >=10:
#         grade = 'Satisfactory'
#     elif points <10:
#         grade = 'Fail'
#     return grade

# test_result = 15
# final_grade = pts_to_grade(test_result)
# print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')

###4.6
# Function that returns the full name of a day of the week
# based on its number
#
# def day_name(day_number):
#     result = ''
#     if day_number == 1:
#         result = 'M'
#     elif day_number == 2:
#         result = 'T'
#     elif day_number == 3:
#         result = 'W'
#     elif day_number == 4:
#         result = 'T'
#     elif day_number ==5:
#         result = 'F'
#     elif day_number ==7:
#         result = 'S'
#     return result

# # Function usage
# print('The name of day 5 in the week is', day_name(5))
# print('The name of day 3 in the week is', day_name(3))
# print('The name of day 7 in the week is', day_name(7))

###4.7

#icao.py

###4.8
def main(): 
    hours = int(input("Enter hours: ")) 
    minutes = int(input("Enter minute: ")) 
    time_format = int(input("Enter time format: ")) 
    time_string(hours, minutes, time_format) 
 
def time_string(hours, minutes, time_format): 
    if time_format == 24: 
        print(f"{hours}:{minutes}") 
    elif time_format == 12: 
        if hours <= 12: 
            print(f"{hours}:{minutes}am") 
        else: 
            hours -= 12 
            print(f"{hours}:{minutes}pm") 
 
 
if __name__ == "__main__": 
    main()
               

