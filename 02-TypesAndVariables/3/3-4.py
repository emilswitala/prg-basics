###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = input('Your speed in km/h: ')
speed_kmh = int(speed_kmh)

speed_ms = speed_kmh/(3.6)
print("Speed in km/h = ", speed_kmh, "Speed in m/s = ", speed_ms)