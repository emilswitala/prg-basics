# decimal to binary

decimal = int(input("Enter your decimal number: "))

binary = ""
n = decimal

while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n //= 2
if binary == "":
    binary = "0"
    
print(f"{decimal}(10)   {binary}(2)")
