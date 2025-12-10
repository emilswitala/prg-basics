structure = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

# make it diagonally 1
# alr...
for i in range(len(structure)):
    structure[i][i] = 1

print(structure)

for row in structure:
    for column in row:
        print(column, end=" ")
    print()

# to make it diagonal I have to change every zero that has the same row and column index to one
# structure is my... structure, it's an array
# an array containing three rows and three columns
# structure[i][i] is just that
# and to print it I have to remember the method: for every row and every column in a row print the column 
# ending with a space
# (so for row in structure and for column in row)