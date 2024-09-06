# exception = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("a: "))
    denominator = int(input("b: "))
    result = numerator / denominator
    # print(numerator/denominator)
    # 5/0 not possible, so we use exception
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("enter only numbers please")
except Exception as e:  # last
    print(e)
    print("something went wrong")
else:
    print(result)
finally:  # used specifically in file handling
    print("This will always execute")