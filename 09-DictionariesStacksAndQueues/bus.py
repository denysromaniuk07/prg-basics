# ##Dictionary

# # student = {
# #    'name': 'John',
# #    'age': 22,
# #    'major': 'Computer Science'
# # }

# # # Accessing a value
# # print(student['name'])

# # # Adding a new key-value pair
# # student['grade'] = 'A'

# # # Modifying an existing value
# # student['age'] = 23

# # # Deleting a key-value pair
# # del student['major']
# # print(student)

# # fruit = {'apple': 3, 'orange':4, 'banana':5}

# # # for item, value in fruit.items():
# # #    print(item)
# # #    print(value)

# # for count in fruit.values():
# #    print(count)

# person = {
#    "name": "Marek",
#    "surname": "Banach",
#    "age": 25,
#    "hobby": ["swimming","excursions"],
#    "married": True,
#    "phone":{"landline":"123444321","mobile":"777888999"}
# }

# print(person['name'])

# print(person['hobby'])

# for i in person.items():
#    print(i)

# person["surname"] == 'Novak'

# person["married"] == False

# person['gender'] = 'male'

# print(person['gender'])

# person["hobby"] += ['bycicle']

# print(person['hobby'])

# person["phone"]['work'] = '873645736487'

# print(person['phone']['work'])

# for key, value in person.items():
#    print(f"{key}:{value}")


# countriesPopulation = [
#    {"name":"Poland", "population":38000000},
#    {"name":"Germany", "population":83000000},
#    {"name":"France", "population":67000000},
#    {"name":"Italy", "population":60000000},
#    {"name":"United Kingdom", "population":66000000}
# ]

# for country in countriesPopulation:
#    print(f"{country['name']} {country['population']}")

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


# for name, phone in phone_book.items():
#    if name[0] == 'D':
#       print(name, phone)

# store ={
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

# sum = 0
# for key, value in store.items():
#    print(key, value)
#    sum += value

# print(sum)

