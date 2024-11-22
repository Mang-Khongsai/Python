# create a textfile file1.txt 
# insert some contents
with open('old_file.txt', 'w') as f:
    f.write("1. Hello World\n")
    f.write("2. Hi World")

    f.close()

# read the file contents
with open("old_file.txt", "r") as f:
    print(f.read())
    f.close()

import os
# rename the existing file 

os.rename('old_file.txt', 'new_file.txt')

if os.path.exists('new_file.txt'):
    print("file renamed successfully")

else:
    print("renamed failed")

