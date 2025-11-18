###
# A program that calculates and prints
# the average grade of a student
#
math = input('Enter your grade from math: ')
art = input('Enter your grade from art: ')
music = input('Enter your grade from music: ')
history = input('Enter your grade from history: ')

math = float(math)
art = float(art)
music = float(music)
history = float(history)

average = (math + art + music + history) / 4
print("Your average grade is: ", average)