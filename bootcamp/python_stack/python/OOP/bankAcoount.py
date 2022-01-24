class BankAccount:
    def __init__(self, int_rate=0.01, balance=0, int_withdraw=5):
        self.account_int_rate = int_rate
        self.account_balance = balance
        self.int_withdraw = int_withdraw # cobrar 5 por tarifa

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        self.account_balance -= self.int_withdraw # cobrar 5 por tarifa
        return self

    def display_account_info(self):
        print(self)

    def yield_interest(self):
        self.account_balance += (self.account_balance * self.account_int_rate)
        return self

class user:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        if (self.account.account_balance < amount+self.account.int_withdraw):
            print(f"No tiene fondos suficientes, Se cobra ${self.account.int_withdraw} al retirar")
        else:
            self.account.withdraw(amount)
            return self

    def display_account_info(self):
        print(f"Saldo: ${self.account.account_balance} y su tasa de interes es de {self.account.account_balance*self.account.account_int_rate}")


guido = user("Guido Python", "guido@python.com")
monty = user("Monty Python", "monty@python.com")

guido.make_deposit(200).make_deposit(100).make_deposit(250).make_withdraw(210).display_account_info()
monty.make_deposit(500).make_deposit(300).make_withdraw(20).make_withdraw(100).make_withdraw(150).make_withdraw(70).display_account_info()