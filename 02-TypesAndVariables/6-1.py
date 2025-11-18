###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = input('Enter your name: ')   # replace Anna with your name
surname = input('Enter your surname: ') # replace May with your surname

name = str(name)
surname = str(surname)

characters_in_name = len(name)
characters_in_surname = len(surname)
characters_in_name = int(characters_in_name)
characters_in_surname = int(characters_in_surname)

all_char = characters_in_surname + characters_in_name 
char_with_space = all_char + 1

print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {all_char} and {char_with_space} with the space in between your name and surname.') # with a space between name and surname