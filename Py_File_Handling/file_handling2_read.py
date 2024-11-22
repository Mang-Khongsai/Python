

# without f.seek()
with open('file.txt', 'r') as f: 
    print(f.read())
    print(f.readline())
    print(f.readlines())
    print("\n\n")
    f.close()


# with f.seek()
with open('file.txt', 'r') as f: 
    print(f.read())
    # f.seek(0)  will help us to read from the start of the index
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())
    f.close()

# using f.tell() : it returns the current file position
with open('file.txt', 'r') as f:
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.tell())
    print("\n\n")
    f.close()

with open('file.txt', 'r') as f: 
    print(f.read(5))
    print("--------")
    f.seek(0)
    print(f.read(10))
    f.close()
