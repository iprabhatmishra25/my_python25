class BankAccount:
    total_accounts=0

    
    def __init__(self, owner , balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self , amount):
        self.balance += amount
        print(f"{self.owner} Deposited:${amount:.2f}")

    def withdraw(self ,amount):
        if amount > self.balance:
            raise ValueError(f"{self.owner} ${amount:.2f} ${self.balance:.2f}")

        self.balance -= amount
        print(f"[{self.owner}] withdraw: $[{self.balance}]")

    def __str__(self):
        return f"{self.owner:<10} balance : ${self.balance:.2f}"

print(f"total account : {BankAccount.total_accounts}")       

acc1= BankAccount("prabhat",150)
acc2 = BankAccount("om",210)
acc3 = BankAccount("raj",180)

print(acc1)
print(acc2)
print(acc3)