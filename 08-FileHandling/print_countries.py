###
# Reads from file, line by line
#

with open('countries.txt', 'r') as file:
    content = file.read()
    i = 1
    for line in content:
        print(f"{i}.", line, end="")
        i += 1