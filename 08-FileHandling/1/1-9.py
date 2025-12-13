###
# Prints employees employed in a specified position.
#
import csv
# Employee List
file_name = 'it_company.csv'


# Position


with open(file_name, 'r') as csvfile:
   content = csv.reader(csvfile, delimiter=',')
   i = 1
   for line in content:
      if 'Software Engineer' in line:
         print(f'{i}.', line)
         i += 1
