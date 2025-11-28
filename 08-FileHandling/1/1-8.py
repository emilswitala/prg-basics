###
# Prints the text and counts the number of words

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

total = 0
for  line in file_lines:
   split_lines = line.split()
   numb = len(split_lines)
   total += numb

print(total)