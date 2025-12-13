# Write a program that displays the first 
# five lines from the it_company.csv file 
# and then prints 'Press Enter key...' 
# in the next line and waits for 
# the Enter key to be pressed. 
# The program repeats printing 
# the next five lines from the file, 
# waiting for the Enter key to be pressed each time.

file_name = "it_company.csv"
chunk = 5

try:
    with open('it_company.csv', 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    current_line = 0

    while current_line < total_lines:
        for line in lines[current_line:current_line + chunk]:
            print(line.strip())
        
        current_line += chunk

        if current_line < total_lines:
            try:
                input("Press Enter...")
            except KeyboardInterrupt:
                print()
                print("Program has been broken by the user")
                break


except FileNotFoundError:
    print("Sorry buddy, that file doesn't exist")
