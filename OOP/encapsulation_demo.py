# Encapsulation restricts access to certain components of an object and can prevent the accidental modification of data.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Deposit amount must be positive."

    def get_balance(self):
        return self.__balance

account = BankAccount("123456")
print(account.deposit(100))  # Output: Deposited 100. New balance: 100
print(account.get_balance())  # Output: 100