###
# Prints employees employed in a specified position.
#
import csv
# Employee List
file_name = 'it_company.csv'


# Position
job_title = 'Software Engineer'

i = 1
with open(file_name, 'r') as csvfile:
   content = csv.reader(csvfile, delimiter=',')
   for line in content:
      if job_title in line:
         print(f'{i}.', line)
         i += 1
