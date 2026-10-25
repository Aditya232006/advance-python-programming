class BankAccount:

    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter


    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")
    
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Error: Insufficient balance.")

   
    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully.")
        else:
            print("Error: Insufficient balance for transfer.")

account1 = BankAccount("Madhuri")
account2 = BankAccount("Priya")

print("----- Initial Account Details -----")
account1.display_balance()
print()
account2.display_balance()

print("\n----- Deposits -----")
account1.deposit(5000)
account2.deposit(3000)

print("\n----- After Deposit -----")
account1.display_balance()
print()
account2.display_balance()

print("\n----- Withdrawal -----")
account1.withdraw(1000)

print("\n----- Transfer -----")
account1.transfer(1500, account2)

print("\n----- Final Account Details -----")
account1.display_balance()
print()
account2.display_balance()