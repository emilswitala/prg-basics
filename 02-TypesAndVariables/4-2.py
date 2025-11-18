###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#

father_income = input("Enter your father's income: ")
mother_income = input("Enter your mother's income: ")
family_members = input('Enter how many family members you have: ')

father_income = int(father_income)
mother_income = int(mother_income)
family_members = int(family_members)

total_income = father_income + mother_income
income_per_person = total_income/family_members

print(f'Total family income is {total_income}, and income per person is {income_per_person}')