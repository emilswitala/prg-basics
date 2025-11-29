import time
import sys

print("wow")

print("sheesh")

print("that's insane")

print(". . .")

text1 = ". . . . . . . . . ."
for char in text1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.3)