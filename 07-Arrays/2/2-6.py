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