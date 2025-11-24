###
# Calculates the sum of the digits in a number
#
def sum_digits(any_number):
    result = 0
    for digit in any_number:
        digit = int(digit)
        result += digit
    return result

any_number = str(abs(int(input('Enter integer number: '))))
print(f'The sum of the digits in the number {any_number} is {sum_digits(any_number)}')