def create_2d_array(x,y):
    return [[1 for j in range(y)] for i in range(x)]

array = create_2d_array(3,5)

for row in array:
    for col in row:
        print(col, end=' ')
    print()
