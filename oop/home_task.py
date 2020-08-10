class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep):
        self.balance = self.balance + dep
        print("Внесение выполнено")

    def withdraw(self, minus):
        if self.balance - minus < 0:
            print("Недостаточно средств!")
        else: 
            self.balance = self.balance - minus
            print("Снятие выполнено")
            
    def __str__(self):
        return f"Владелец счёта:   {self.owner} \nБаланс счёта: {self.balance}"


acct1 = Account('Влад',100)
print(acct1)

print(acct1.owner)
print(acct1.balance)

print(acct1.withdraw(75))
print(acct1.deposit(50))

print(acct1.owner)
print(acct1.balance)

print(acct1.withdraw(500))

print(acct1.balance)