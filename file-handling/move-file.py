import os

destination = "test.txt"
source = "/home/vedeshpadal/Desktop/hi.txt"
# you can also move a Directory
try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")
