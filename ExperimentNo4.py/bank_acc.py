class BankAccount:
    counter = 1000

    def __init__(self, name):
        self.account_holder = name
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.account_holder, self.balance)

    def transfer(self, amount, other):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other.balance += amount
        else:
            print("Insufficient balance")

a1 = BankAccount("Amit")
a2 = BankAccount("Rahul")

a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(1000, a2)

a1.display_balance()
a2.display_balance()