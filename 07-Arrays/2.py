###2.2

# 3x3 Tic-Tac-Toe board
# tic_tac_toe_board = [
#    ['X', 'O', 'X'],
#    [' ', 'X', 'O'],
#    ['O', ' ', 'X']
# ]

# for row in tic_tac_toe_board:
#    for cell in row:
#       print(cell, end=" ")
#    print()

# print(tic_tac_toe_board)

###2.3

# Weekly expenses for different categories
# [Food, Transport, Utilities]
# monthly_expenses = [
#     [200, 50, 100],  # Week 1
#     [180, 60, 110],  # Week 2
#     [220, 55, 105],  # Week 3
#     [210, 65, 95]    # Week 4
# ]

# totalFood = 0
# totalTransport = 0
# totalUtilities = 0
# totalWeek = []
# total = 0

# # Calculate totals
# for week in monthly_expenses:
#     totalFood += week[0]
#     totalTransport += week[1]
#     totalUtilities += week[2]
#     totalWeek.append(sum(week))  
# total = sum(totalWeek)  

# print('MONTHLY EXPENSES')
# print('----------------')
# print('Food:', totalFood)
# print('Transport:', totalTransport)
# print('Utilities:', totalUtilities)
# print('Week 1:', totalWeek[0])
# print('Week 2:', totalWeek[1])
# print('Week 3:', totalWeek[2])
# print('Week 4:', totalWeek[3])
# print('----------------')
# print('TOTAL:', total)


####2.4
# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
# meal_plan = [
#    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
#    ["Pancakes", "Sandwich", "Steak"],
#    ["Smoothie", "Chicken Wrap", "Salmon"],
#    ["Eggs", "Pasta", "Soup"],
#    ["Toast", "Burrito", "Pizza"],
#    ["Cereal", "Salad", "Fish Tacos"],
#    ["Bagel", "Rice and Beans", "Stir-fry"]
# ]

# # Returns a week day name
# def weekday(n):
#    weekdays = ["Monday", "Tuesday", "Wednesday",
#       "Thursday", "Friday", "Saturday", "Sunday"]
#    return weekdays[n-1]

# # Returns a string with day meal names
# # separated by comma
# def day_meal_plan(meal_plan, day_number):
#    result = ",".join(meal_plan[day_number-1])
#    return result

# # Prints weekly meal plan
# print("WEEKLY MEAL PLAN")
# print("(Breakfast, Lunch, Dinner)")
# print("==========================")
# for i in range(1,8):
#    print(f"{weekday(i)}: {day_meal_plan(meal_plan, i)}")

###2.5

# cinema_seats = [
#    ['A', 'A', 'B', 'A', 'A'],
#    ['A', 'B', 'B', 'A', 'A'],
#    ['A', 'A', 'A', 'A', 'B'],
#    ['B', 'A', 'A', 'A', 'A'],
#    ['A', 'B', 'A', 'A', 'A']
# ]

# def seats_total(seats):
#    seats = len(sum(cinema_seats, []))
#    return seats

# def seats_available(seats):
#    avaible =0
#    for row in seats:
#       avaible += row.count("A")
#    return avaible

# def seats_booked(seats):
#    booked = 0
#    for row in seats:
#       booked += row.count("B")
#    return booked

# def seat_status(seats, row, place):
#    return seats[row][place]

# print('CINEMA INFORMATION TABLE')
# print('Total seats:', seats_total(cinema_seats))
# print('Seats available', seats_available(cinema_seats))
# print('Seats booked:', seats_booked(cinema_seats))
# print('Seat in row 1, place 1:', seat_status(cinema_seats, 0,0))
# print('Seat in row 5, place 5:', seat_status(cinema_seats, 4,4))
# print('Seat in row 3, place 5:', seat_status(cinema_seats, 2,4))


###2.6

# matrix = [
#    [0,0,0],
#    [0,0,0],
#    [0,0,0]
# ]

# for i in range(len(matrix)):
#    matrix[i][i]=1

# for row in matrix:
#    print(" ".join(map(str,row)))
