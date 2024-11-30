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

arr = [-15, 8,-31,47,-2,19]

max_num = arr[0]
min_num = arr[0]

for n in arr:
    if n > max_num:
        max_num =n
    if n<min_num:
        min_num = n
print (max_num)
print (min_num)