arr = [2, 6, 4, 9, 7]

for i in arr:
    print(f"{i}. {'*'*i}")

# or

def star(n):
    return n*'*'

for i in range(len(arr)):
    print(f'{arr[i]}. {star(arr[i])}')