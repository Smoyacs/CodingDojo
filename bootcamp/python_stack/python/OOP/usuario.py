class user:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    # Agrega metodo de deposito
    def make_deposit(self, amount):
        self.account_balance += amount

    # Agrega meotodo de giro
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    # Agrega metodo de impresion de saldo
    def display_user_balance(self):
        print(f"Usuario: {self.name}, Saldo: $ {self.account_balance}")


    # Agrega metodo de transferencia entre usuarios
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"\nTransferencia de usuario {self.name} a usuario {other_user.name}")
        print(f"Usuario: {self.name}, Saldo: $ {self.account_balance}")
        print(f"Usuario: {other_user.name}, Saldo: $ {other_user.account_balance}")


# 3 instancias de la clase usuario
guido = user("Guido van Rossum", "guido@python.com")
monty = user("Monty Python", "monty@python.com")
seba = user("Sebastian Moya", "seba@python.com")


# primer usuario 3 depositos y un retiro luego mostrar saldo

guido.make_deposit(100)
guido.make_deposit(300)
guido.make_deposit(50)

guido.make_withdrawal(50)

guido.display_user_balance()

# segundo usuario 2 depositos, 2 retiros luego mostrar saldo

monty.make_deposit(100)
monty.make_deposit(500)

monty.make_withdrawal(200)
monty.make_withdrawal(20)

monty.display_user_balance()

# tercer usuario 1 deposito, 3 retiros luego mostrar saldo

seba.make_deposit(1500)

seba.make_withdrawal(250)
seba.make_withdrawal(50)
seba.make_withdrawal(360)

seba.display_user_balance()

# BONIFICACION metodo transfer. transferencia dele primer usuario al tercer usuario luego mostras ambos saldos
guido.transfer_money(seba, 100)

seba.transfer_money(monty, 340)