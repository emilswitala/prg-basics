###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('pets.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()
sort_file_names = sorted(file_lines)
# prints the array
i = 1
for line in sort_file_names:
   print(f'{i}.', line)
   i += 1