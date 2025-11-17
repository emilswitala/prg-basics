###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''


for char in plain_text:
    # read the character's code (use ord())
    letter_code = ord(char)
    # add one to the character's code
    if letter_code != 32:
        encrypted_code = letter_code + 1
    # replace new character code with its
    # corresponding character (use chr())
        encrypted_letter = chr(encrypted_code)
    # add encrypted character to encrypted text
        encrypted_text = encrypted_text + encrypted_letter
    else:
        encrypted_text += char
    

print(plain_text)
print(encrypted_text)