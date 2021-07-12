class Account:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner} \nAccount Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal Accepted.")
        else:
            print("Funds Unavailable!")

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)