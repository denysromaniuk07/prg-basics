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
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders.sort()

# Write data to the file
with open(file_name, 'w') as file:
   for item in seven_wonders:
      file.write(item + '\n')
