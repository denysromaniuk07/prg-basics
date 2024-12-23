###5.1

# translations = {
#    'computer': 'komputer',
#    'mouse': 'myszka',
#    'keyboard': 'klawiatura',
#    'printer': 'drukarka'
# }

# def translate_word(word):
#     if word in translations:
#         return translations[word]
#     else:
#         return word

# print(translate_word('mouse'))  

###5.4

# winter_semester = {
#    "math":60,
#    "programming":30,
#    "history":15
# }

# def total_number_of_hours(hours):
#     total = 0
#     for subject, hours_per_subject in hours.items():
#         total += hours_per_subject
#     return total

# print(total_number_of_hours(winter_semester))

###5.5

# paragraph = "cat dog mouse cat rat cat mouse"

# def count_word(text):
#     words = text.split()
#     word_counts = {}
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts

# print(count_word(paragraph))

###5.6

# basic_data = {
#    "name":"Barbara",
#    "age":21
# }

# advanced_data = {
#    "status":"student",
#    "married":False,
#    "interest":["reading","swimming"]
# }

# def merge_data(data1, data2):
#     merged_data = data1.copy()
#     merged_data.update(data2)
#     return merged_data

# print(merge_data(basic_data, advanced_data))

###5.7

# hotels_in_Krakow = [
#    {"name":"Sky","price":320.00},
#    {"name":"Metropol","price":480.00},
#    {"name":"New Port","price":420.00},
#    {"name":"Aparthotel","price":390.00}
# ]

# hotels_in_Sopot = [
#    {"name":"Focus","price":510.00},
#    {"name":"Aqua","price":345.00},
#    {"name":"La Boutique","price":390.00},
#    {"name":"Marina","price":410.00}
# ]


# def hotel_list(hotels):
#     return [hotel["name"] for hotel in hotels]

# def avg_price(hotels):
#     total_price = sum([hotel["price"] for hotel in hotels])
#     avg = total_price / len(hotels)
#     return avg

# def comapare_price(hotel1, hotel2):
#     if avg_price(hotel1) < avg_price(hotel2):
#         return "Krakow"
#     else:
#         return "Sopot"


# print("Hotels in Krakow: ", hotel_list(hotels_in_Krakow))
# print("Avarege hotel price in Krakow:", avg_price(hotels_in_Krakow))
# print("Hotels in Sopot: ", hotel_list(hotels_in_Sopot))
# print("Avarege hotel price in Sopot:", avg_price(hotels_in_Sopot))
# print("Cheper hotel price in",comapare_price(hotels_in_Krakow, hotels_in_Sopot) )


###5.8

# # Price list
# prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# # Shopping cart with quantities
# cart = {'juice': 3, 'bread': 1, 'milk': 2}

# # Calculate total cost
# def calculate_total_cost(prices, cart):
#     total = 0
#     for item, quantity in cart.items():
#         total += prices[item] * quantity
#     return total

# print("total cost:", calculate_total_cost(prices, cart))

###5.9

# file_name_vehicle = 'vehicle.txt'
# file_name_province = 'province.csv'

# with open(file_name_vehicle, 'r', encoding='utf-8') as file:
#     car_plates = file.readlines()

# numbers_data = [line.strip() for line in car_plates]

# regions_dict = {}

# with open(file_name_province, 'r', encoding='utf-8') as file:
#     for line in file:
#         letter, name = line.strip().split(',')
#         regions_dict[letter] = name

# car_count_by_province = {region: 0 for region in regions_dict.values()}


# for plate in car_plates:
#     province_code = plate[0]
#     if province_code in regions_dict:
#         province_name = regions_dict[province_code]
#         car_count_by_province[province_name] += 1
        
        
# for province, count in car_count_by_province.items():
#     print(f"{province}: {count} cars")





