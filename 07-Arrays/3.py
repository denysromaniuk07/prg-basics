##3.1

# arr = [34,7,19,4,21,8]

# count =0 
# i = 0
# while i < len(arr):
#     if arr[i] % 2 == 0:
#         count+=1
#     i+=1

# print(count)

##3.2

# arr = [15,8,31,47,2,19]

# for i in range(len(arr)-1,-1,-1):
#     print(arr[i], end=" ")

##3.3 

# arr = [8,2,5,1,9]
# newArr = []

# for i in range(len(arr)):
#     newArr.append(arr[i]**2)
# print (newArr)

##3.4

# arr = [-15, 8,-31,47,-2,19]

# max_num = arr[0]
# min_num = arr[0]

# for n in arr:
#     if n > max_num:
#         max_num =n
#     if n<min_num:
#         min_num = n
# print (max_num)
# print (min_num)


###3.5
# arr = [1,2,3,4,5]

# print(arr)
# arr[0] -=1
# print(arr)
# arr[-1] +=4
# print(arr)
# arr[2] *=2
# print(arr)

###3.6

# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#

# def weekday(n):
#     weekdays = ["Monday", "Tuesday", "Wednesday",
#          "Thursday", "Friday", "Saturday", "Sunday"]
#     return weekdays[n]

# print(weekday(0))
# print(weekday(3)) 
# print(weekday(6)) 

### 3.7
# Prints shopping list
#
# shopping_list = [
#    "milk", "bread", "eggs", "butter", "cheese",
#    "tomatoes", "potatoes", "carrots", "onions", "garlic"
# ]

# for item in shopping_list:
#    print(item)
