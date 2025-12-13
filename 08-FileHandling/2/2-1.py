# Program to write movie details to a text file

# Variables containing movie details
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"
crazy_fr = 'Insane vibes'

# Name of the file to write to
file_name = 'movie_details.txt'

# Writing movie details to the file
with open(file_name, 'w') as file:
   file.write(f"Movie Title: {movie_title}\n")
   file.write(f"Director: {director}\n")
   file.write(f"Lead Actor: {lead_actor}\n")
   file.write(f'Vibes: {crazy_fr}\n')
   
print(f"Movie details have been written to {file_name}.")