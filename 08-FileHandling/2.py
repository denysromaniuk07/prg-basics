###2.1
# Program to write movie details to a text file

movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

file_name = 'movie_details.txt'

with open(file_name, 'w') as file:
   file.write(f"Movie Title: {movie_title}\n")
   file.write(f"Director: {director}\n")
   file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")

###2.3
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file) as file:
   content = ... .read()
...
...

# write the content to the target file (copy)
with ... as ...:
   ... .write(...)
