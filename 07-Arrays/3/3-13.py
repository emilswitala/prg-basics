number = input('Number: ')
array = input('Array: ')

def occurs(number,array):
    for item in array:
        if item == number:
            return True
    return False
    
def occurs2(number,array):
    return number in array

print(occurs(number,array))
print(occurs2(number,array))

