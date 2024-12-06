###2.1
# Program to write movie details to a text file

# movie_title = "Inception"
# director = "Christopher Nolan"
# lead_actor = "Leonardo DiCaprio"

# file_name = 'movie_details.txt'

# with open(file_name, 'w') as file:
#    file.write(f"Movie Title: {movie_title}\n")
#    file.write(f"Director: {director}\n")
#    file.write(f"Lead Actor: {lead_actor}\n")

# print(f"Movie details have been written to {file_name}.")

###2.2
# Writes Seven Wonders of the World to a file
#
# seven_wonders = [
#    "Great Wall of China",
#    "Petra",
#    "Christ the Redeemer",
#    "Machu Picchu",
#    "Chichen Itza",
#    "Roman Colosseum",
#    "Taj Mahal"
# ]

# # Name of the file to write to
# file_name = 'seven_wonders.txt'

# # Sort data alphabetically
# seven_wonders.sort()

# # Write data to the file
# with open(file_name, 'w') as file:
#    for item in seven_wonders:
#       file.write(item + '\n')

###2.3
###
# Makes a copy of a text file
#

# # file names
# original_file = 'healthy_lifestyle.txt'
# target_file = 'copy_healthy_lifestyle.txt'

# # read the content of the original file
# with open(original_file, 'r') as original:
#    content = original.read()

# # write the content to the target file (copy)
# with open(target_file, "w") as target:
#    target.write(content)


###2.4
# Saves to a file a list of employees working at a specified position.
#

# # file names
# employees_file = 'it_company.csv'
# position_file = 'software_engineer.txt'

# # Position
# job_title = 'Software Engineer'

# # write selected employees to a file
# with open(employees_file, "r") as file:
#    with open(position_file, "w") as position:
#       for line in file:
#          if job_title in position:
#             position.write(line)

###2.5
# Creates a shopping list based on product names
# entered from the keyboard.
#

# shopping list file name
shopping_list = 'shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, product_name):
   with open(file_name,'a') as file:
      file.write(product_name + '\n')

# Takes next product name from the keyboard
product = " "
while product != "0":
   product = input('Enter product name (0 stops): ')
   if product == '0':
      break # stops entering food names ('while' breaks)
   else:
      add_product(shopping_list, product)