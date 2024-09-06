class MathOperations:
    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathOperations.add(5, 3))      # Output: 8
print(MathOperations.multiply(5, 3))  # Output: 15