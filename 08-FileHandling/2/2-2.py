###
# Writes Seven Wonders of the World to a file
# in alphabetical order in a separate line
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
sorted_alphabetically = sorted(seven_wonders)
print(sorted_alphabetically)

# Write data to the file
with open(file_name, 'w') as file:
    for item in sorted_alphabetically:
        file.write(f'{item}\n')