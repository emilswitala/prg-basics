###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = input('Enter your text: ')
encrypted_text = ''
your_key = int(input('Enter your key (1-25): '))

if your_key >= 1 and your_key <= 25:
    for char in plain_text:
        # read the character's code (use ord())
        letter_code = ord(char)
        # add one to the character's code
        if letter_code != 32:
            encrypted_code = letter_code + your_key
        # replace new character code with its
        # corresponding character (use chr())
            encrypted_letter = chr(encrypted_code)
        # add encrypted character to encrypted text
            encrypted_text += encrypted_letter
        else:
            encrypted_text += char 

    print(f'Your message: {plain_text}')
    print(f'Shh!! Top secret!: {encrypted_text}')
else: 
    print('Please choose a different key!')