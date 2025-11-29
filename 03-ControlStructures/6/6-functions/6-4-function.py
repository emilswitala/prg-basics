# Defines an appropriate password length
#

password = input("Enter your password: ")

def appropriate_length(password):
    i = 0
    count = 0
    if len(password) >= 12:
        appropriate_length = True
    elif len(password) < 12:
        appropriate_length = False
    return appropriate_length

print("Your password is long enough: ", appropriate_length(password))
    