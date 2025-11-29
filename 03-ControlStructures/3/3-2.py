###
# Checking login and password
#
login = "joe"
password = "twujstary"

entered_login = input('Repeat login: ')
entered_password = input('Repeat password: ')

if login == entered_login and password == entered_password:
    print('Login and password are correct, you have been logged in.')
else:
    print('Login or password do not match. Please try again.')