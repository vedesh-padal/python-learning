"""
default arguments = A default value for certain parameters
                    default is used when that argument is ommitted
                    make your functions more flexible, reduces # of
                    arguments
                    1. positional, 2. default, 3. keyword, 4. arbitrary
"""

from time import sleep
def count(end, start = 0):  # non-default arguments should follow default arguments
    for x in range(start, end+1):
        print(x)
        sleep(1)
    print("Done")
count(30,15)