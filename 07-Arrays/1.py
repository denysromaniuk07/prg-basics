###1.4

# arr = [2, 3, 7, 5, 4]

# print(arr)
# print('Number of elements:', len(arr))
# print('First value:', arr[0])
# print('Second value:', arr[1])
# print('Last value:', arr[len(arr) - 1])
# print('Last but one value:', arr[len(arr) - 2])
# print('Sum of the first and last value:', arr[0] + arr[len(arr) - 1])
# print('Middle value:', arr[len(arr) // 2])
# print('All array values:', end=' ')
# for value in arr:
#     print(value, end=' ')


####1.5

# arr = [1, 2, 3, 4, 5]

# print('Array:', arr)
# arr[0] -= 1
# print('Array:', arr)
# arr[len(arr) - 1] += 4
# print('Array:', arr)
# arr[len(arr) // 2] *= 2
# print('Array:', arr)

####1.6

# def weekday(n):
#     weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     return weekdays[n - 1]

# print(weekday(1))
# print(weekday(4))
# print(weekday(7))

###1.7

# shopping_list = [
#     "milk", "bread", "eggs", "butter", "cheese",
#     "tomatoes", "potatoes", "carrots", "onions", "garlic"
# ]

# for item in shopping_list:
#     print(item)

###1.8

# computer_games = [
#     "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
#     "League of Legends", "Valorant", "Grand Theft Auto V", 
#     "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
# ]

# computer_games.sort()
# counter = 1

# index = 0
# while index < len(computer_games):
#     print(f"{counter}. {computer_games[index]}")
#     counter += 1
#     index += 1

### 1.9

# polish_license_plates = [
#     'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
#     'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
#     'KK54985', 'LU4864U'
# ]

# counter = 1

# for car_number in polish_license_plates:
#     if car_number.startswith('KR') or car_number.startswith('KK'):
#         print(f"{counter}. {car_number}")
#         counter += 1


###1.10
# Prints test statistics
#
# test_results = [
#    False, True, False, True, True,
#    True, True, False, True, True,
#    False, True, True, True, False
# ]

# # calculates the number of test questions
# question_number = len(test_results)

# # calculates the number of correct answers
# correct_answers = 0
# for answer in test_results:
#    if answer == True:
#       correct_answers += 1


# # calculates the number of incorrect answers
# incorrect_answers = 0
# for answer in test_results:
#    if answer == False:
#       incorrect_answers += 1

# # calculates the percentage of correct answers
# percentage_correct = (correct_answers / question_number) * 100

# print('TEST STATISTICS')
# print('===============')
# print('Number of questions:', question_number)
# print('Number of correct answers:', correct_answers)
# print('Number of incorrect answers:', incorrect_answers)
# print('Percentage of correct answers:', round(percentage_correct, 2), '%')

###1.11
# The weather station report
#
# temperatures = [
#  3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
#  4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
#  -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
# ]

# # number of mesaurements
# mesaurements = len(temperatures)

# # calculates average temperature
# temp_total = 0
# for temp in temperatures:
#    temp_total += temp
# avg_temp = temp_total/mesaurements

# # calculates min and max temperatures
# min_temp = min(temperatures)
# max_temp = max(temperatures)

# # calculates number of days with negative temp
# negative_temp = 0
# i = 0
# while i < mesaurements:
#    if temperatures[i] < 0:
#       negative_temp+=1
#    i+=1

# # prints out month report
# print("TEMPERATURE REPORT")
# print("Month: March")
# print(f"Number of measurements: {mesaurements}")
# print(f"Average temperature in the month: {avg_temp:.2f}")
# print(f"Minimum temperature: {min_temp}")
# print(f"Maximum temperature: {max_temp}")
# print(f"Number of days with negative temperature: {negative_temp}")

###1.12

# categories = ["Food", "Transport", "Rent","Entertainment"]
# expenses = [500, 150, 1000, 200]

# maxExpenses = max(expenses)
# maxIndex = expenses.index(maxExpenses)
# print(f"Category with the highest expenses: {categories[maxIndex]}")

###1.13

# # Prices of 10 products in the computer store (in currency units)
# product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# # Number of units available for each product
# product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# value = 0

# for i in range(len(product_prices)):
#     value += product_prices[i] * product_quantities[i]

# print(f"The total value of all goods in the store is: {value}")

###1.15

# Функція сортування бульбашкою
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):  
#         for j in range(0, n-i-1):  
#             if arr[j] > arr[j+1]:  
#                 arr[j], arr[j+1] = arr[j+1], arr[j]  
#     return arr

# car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
# bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

# print("Car fuel consumption:", car_fuel_consumption)
# sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
# print("After sort:", sorted_car_fuel_consumption)

# print("Bank transaction before sort:", bank_transactions)
# sorted_bank_transactions = bubble_sort(bank_transactions)
# print("After sort:", sorted_bank_transactions)

###1.16

# # Sort the data from lowest to highest value
# distances_traveled = [120, 150, 180, 90, 200, 175, 160]
# sorted_distances = sorted(distances_traveled)
# print(sorted_distances)
# # Sort the data in descending order, from highest to lowest value
# daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
# sorted_daily_temperatures = sorted(daily_temperatures, reverse=True)
# print(sorted_daily_temperatures)
# # Sort the data in ascending order
# file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
#    "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
# sored_file = sorted(file_names)
# print(sored_file)