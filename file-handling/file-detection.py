import os

# path = "C:\\Users\\HiteshPadal\\Documents\\VedeshPadal\\Learning\\Python-BroCode\\inUbuntu\\Brocode-Python\\file-handling\\test.txt"
path = "test.txt"
if os.path.exists(path):
    print("That location exisits!")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
       print("that is a directory")
else:
    print("that location doesn't exist")