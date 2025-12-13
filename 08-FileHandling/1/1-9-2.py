file_name = 'it_company.csv'

with open(file_name, 'r') as file:
    i = 1
    for line in file:
        if 'Software Engineer' in line:
            print(f"{i}.", line)
            i += 1

with open(file_name, 'r') as file:
    list = []
    i = 1
    for line in file:
        if 'Software Engineer' in line:
            list.append(line.strip())
    for row in list:
        print(f"{i}. ", row)
        i += 1
