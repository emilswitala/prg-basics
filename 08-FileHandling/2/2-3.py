###
# Makes a copy of a text file
# read and copy

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as file:
   content = file.read()


# write the content to the target file (copy)
with open(target_file, 'w') as copy:
   copy.write(content)

print(f"A copy of {original_file} has been created.")