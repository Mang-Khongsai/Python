import os



# change directory
os.chdir("./Stipend_dir")
print(os.getcwd())

# create file and see where it is stored
if os.path.exists('number.txt'):
    print("file already exist.") 
else:
    with open('number.txt', 'w') as f:
        f.write('1\n')
        f.write('2\n')
        f.write('3')
        f.close()


# change directory
os.chdir("..")
print(os.getcwd())