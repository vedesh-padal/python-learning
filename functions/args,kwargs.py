"""
args = allows you to pass multiple non-key arguments
kwargs = allows you to pass multiple keyword-arguments
    * unpacking operator
    1. positional 2. default 3. keyword 4. arbitrary
"""


# def add(a,b):
#     return a+b
#
# print(add(1,3))
# BUT WHAT IF WE WANT TO USE MORE ARGUMENTS, THEN COMES TO PICTURE KWARGS


def add(*args):
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3))

print("IT'S THE TIME FOR KWARGS")


def print_address(**kwargs):
    print(type(kwargs))
    for value in kwargs:
        print(value)
    print()
    for value in kwargs.values():
        print(value)
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="ramnagar",
              H_No="1-6-114/6/1",
              city="Armur",
              state="Telangana", zip=503224)

print("ITS TIME FOR EXERCISE AND USE BOTH\n")


def shipping_label(*args, **kwargs):  # SYNTAX-ERROR won't work if you place kwargs first
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print(f"\n{kwargs.get('street')}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="ramnagar",
               H_No="1-6-114/6/1",
               city="Armur",
               state="Telangana", zip=503224)
