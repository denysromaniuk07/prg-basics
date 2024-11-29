###1.6
# Reads the entire contents of a file
#
# def read_from_file(name):
#    with open(name, 'r') as file:
#       content = file.read()
#    return content

# # reads the entire file
# file_content = read_from_file('countries.txt')

# # splits the entire file contents into lines
# # and stores them in an array
# file_lines = file_content.splitlines()
# filesort = sorted(file_lines)
# # prints the array
# for line in filesort:
#    print(line)        

###1.7
# Reads the entire contents of a file
#
# def read_from_file(name):
#    with open(name) as file:
#       content = file.read()
#    return content

# # reads the entire file and splits lines into array
# file_content = read_from_file('car_park.txt')
# file_lines = file_content.splitlines()

# # calculates the total number of cars parked
# total = 0
# for line in file_lines:
#    total += int(line)

# print('Total cars parked:', total)

###1.8

# def read_from_file(name):
#     with open(name) as file:
#         content = file.read()
#     return content

# file_content = read_from_file('pets.txt')
# file_lines = file_content.split(" ")

# print(len(file_lines))

###1.9
# Prints employees employed in a specified position.
#

# Employee List
# file_name = 'it_company.csv'

# # Position
# job_title = 'Software Engineer'

# # Open the CSV file for reading
# with open(file_name, 'r') as file:
#     count = 1
#     for line in file:
#         if job_title in line:
#             print(f"{count}. {line.strip()}")
#             count += 1

