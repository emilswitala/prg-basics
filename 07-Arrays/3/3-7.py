arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = arr[0]

for name in arr:
    if len(name) > len(longest):
        print(name)