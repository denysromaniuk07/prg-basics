# fruits = {'apple': 3, 'banana': 5, 'orange': 2}

# # Iterating over keys
# for fruit in fruits:
#    print(fruit)

# # Iterating over values
# for count in fruits.values():
#    print(count)

# # Iterating over key-value pairs
# for fruit, count in fruits.items():
#    print(f"The count of {fruit} is {count}")

##1.3

# mobile = {
#     "OS": "IOS",
#     "Brand": "Iphone",
#     "Model": "14 PRO MAX",
#     "Storage": "256GB",
#     "RAM": "8GB",
#     "Camera": "64MP"
# }
# for key,value in mobile.items():
#    print(f"{key} : {value}")

##1.4

# person = {
#    "name": "Marek",
#    "surname": "Banach",
#    "age": 25,
#    "hobby": ["swimming","excursions"],
#    "married": True,
#    "phone":{"landline":"123444321","mobile":"777888999"}
# }

# print(person["name"])

# print(person["hobby"])

# for key, value in person.items():
#     print(f"{key}: {value}")

# person["surname"] = "Novak"

# print(person["surname"])

# person["meriied"] = True

# person["phone"]["work"] ='313131444'

##1.5

# countries = [
# {"name":"Poland", "population":38000000},
# {"name":"Ukraine", "population":40000000},
# {"name":"Rosia", "population":0},
# {"name":"Latvia", "population":24400000},
# {"name": "Canada", "population": 400000000},
# ]

# for country in countries:
#     print(f"{country['name']}\t{country['population']}")

##1.6
###!!!!!!
# phone_book = {
#    'John': '555-1234',
#    'David': '555-5678',
#    'Bob': '555-8765',
#    'Charlie': '555-4321',
#    'Diana': '555-9876',
#    'Eve': '555-6543',
#    'Frank': '555-3456',
#    'Grace': '555-7890',
#    'Hank': '555-1111',
#    'Ivy': '555-2222',
#    'Jack': '555-3333',
#    'Daniel': '555-4444',
#    'Liam': '555-5555',
#    'Mia': '555-6666',
#    'Nina': '555-7777',
#    'Oscar': '555-8888',
#    'Paul': '555-9999',
#    'Dominic': '555-1010',
#    'Rachel': '555-2020',
#    'Sam': '555-3030'
# }

# for name, number in phone_book.items():
#     if name[0] == "D":
#         print(f"{name}: {number}")

###1.7
# list = {
# 'Laptop': 15,
# 'Desktop PC': 10,
# 'Monitor': 25,
# 'Keyboard': 50,
# 'Mouse': 60,
# 'External Hard Drive': 30,
# 'Printer': 12,
# 'Router': 20,
# 'USB Flash Drive': 100,
# 'Graphics Card': 8
# }

# count =0
# for key in list:
#     print(f"{key}")

# for value in list.values():
#     count+=value
    
# print(count)

###1.8

price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}


print("Products and prices before the discount:")
total_before_discount = 0
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")
    total_before_discount += price

print(f"Total value before discount: ${total_before_discount:.2f}")


discounted_price_list = {product: round(price * 0.90, 2) for product, price in price_list.items()}


print("\nProducts and prices after the 10% discount:")
total_after_discount = 0
for product, price in discounted_price_list.items():
    print(f"{product}: ${price:.2f}")
    total_after_discount += price

print(f"Total value after discount: ${total_after_discount:.2f}")
