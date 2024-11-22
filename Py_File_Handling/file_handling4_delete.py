import os


# check if file exists
if os.path.exists("new_file.txt"):
    # read file
    with open("new_file.txt", 'r') as f: 
        print(f.read(),"\n\n")
        f.close()
else:
    print("file not found\n\n")


# remove the file now
if os.path.exists('new_file.txt'):
    os.remove('new_file.txt')
    print("file successfully removed..")
else:
    print("file not found..")





