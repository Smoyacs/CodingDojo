class user:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    # Agrega metodo de deposito
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # Agrega meotodo de giro
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # Agrega metodo de impresion de saldo
    def display_user_balance(self):
        print(f"Usuario: {self.name}, Saldo: $ {self.account_balance}")
        return self

    # Agrega metodo de transferencia entre usuarios
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"\nTransferencia de usuario {self.name} a usuario {other_user.name}")
        print(f"Usuario: {self.name}, Saldo: $ {self.account_balance}")
        print(f"Usuario: {other_user.name}, Saldo: $ {other_user.account_balance}")
        return self

# 3 instancias de la clase usuario
guido = user("Guido van Rossum", "guido@python.com")
monty = user("Monty Python", "monty@python.com")
seba = user("Sebastian Moya", "seba@python.com")

# Actualiza tu asignación anterior(USUARIOS.PY) para que los métodos de cada instancia estén encadenados

guido.make_deposit(100).make_deposit(600).make_deposit(300).make_withdrawal(520).display_user_balance()
