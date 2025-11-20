###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# determine temperature in Celsius
# calculate in Kelvin and Fahrenheit
# print results

temp_c = float(input('Enter the temperature in Celsius: '))

temp_k = temp_c + 273.15
temp_f = (temp_c * 9/5) + 32

print(f'The thermometer reads: {temp_c}°C, {temp_k}K, {temp_f}°.')