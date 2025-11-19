## Vehicle speed on a highway in Poland must be between 40 and 140 km/h

speed = int(input('Enter vehicle speed: '))

speed_okie = speed >= 40 and speed <= 140
speed_not_okie = speed < 40 and speed > 140

print(f'Speed is valid: {speed_okie}')