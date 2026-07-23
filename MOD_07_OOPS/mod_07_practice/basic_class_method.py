# CREATE CLASS

class bankaccount:
    def __init__(self, owner , balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount
        print(f"[{self.owner}] Deposited: ${amount:2f}")

    def withdraw(self , amount):
        if amount > self.balance:
            raise ValueError(f"[{self.owner}]")
        self.balance -= amount
        print("[{self.owner}] withdraw : ${amount:.2f}")

    def __str__(self):
        return f"account owner:{self.owner:<10} | balance : ${self.balance:.2f}"


acc1 = bankaccount("prabhat", 15000)
acc2 = bankaccount("om")

print(acc1)
print(acc2)

    