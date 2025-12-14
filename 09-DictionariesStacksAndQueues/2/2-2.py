# Set Operations:
# & (Intersection): finds common elements between two sets
# | (Union): unites two sets while excluding duplicates
# - (Difference): finds elements present in one set but not the other
# ^ (Symmetric Difference): finds elements present in either set but not both
# .issubset(): checks if one set is a subset of another (so all of its elements
# are in the other set)


# The following program removes duplicate email addresses. 
# Complete and run the program.

emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
unique_emails = set(emails)  # Removes duplicates
print(unique_emails) # basically it made a set out of an array from my understanding
# and a set is an unordered list that excludes all duplicates