import os


# create a folder/directory
if os.path.exists('Stipend_dir'):
    print("directory already exists...!")
else:
    os.mkdir('Stipend_dir')
    print("new directory created.")


# check the absolute directory path
print("direcotry path is: ",os.path.abspath("Stipend_dir"))