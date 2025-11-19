## Trees with circumference under 50 cm cannot be cut down

circumference = int(input('Enter the circumference of your tree in cm: '))

okie = circumference >= 50 
not_okie = circumference < 50

print(f'Can you cut down that tree?: {okie}')