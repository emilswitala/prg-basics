# SURVEY Are you interested in computer science? (y/n): y
# Do you like playing computer games? (y/n): n
# Do you have an Instagram account? (y/n): y

# SURVEY RESULTS Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes
print("SURVEY")
q_one = input("Are you interested in computer science? (y/n): ") == "y"
q_two = input("Do you like playing computer games? (y/n): ") == "y"
q_three = input("Do you have an Instagram account? (y/n): ") == "y"

if q_one:
    q_one = "Yes"
else:
    q_one = "No"

if q_two:
    q_two = "Yes"
else:
    q_two = "No"

if q_three:
    q_three = "Yes"
else:
    q_three = "No"

print("SURVEY RESULTS")
print("Intereseted in computer science: ", q_one)
print("Playing computer games: ", q_two)
print("Has an instagram account: ", q_three)
