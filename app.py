import os


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        self.id = self.generate_id()

    def generate_id(self):
        
        return self.owner[:4].upper() + "1234"

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Depositado: R$ {amount:.2f}")
        return f"Depositado R$ {amount:.2f} con éxito!"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Saldo insuficiente."
        self.balance -= amount
        self.transactions.append(f"Retirado: R$ {amount:.2f}")
        return f"Retirado R$ {amount:.2f} con éxito!"

    def get_statement(self):
        statement = "\n".join(self.transactions)
        return f"Extracto:\n{statement}\nSaldo final: R$ {self.balance:.2f}"

    def transfer(self, other_account, amount):
        if amount > self.balance:
            return "Saldo insuficiente para la transferencia."
        self.balance -= amount
        other_account.balance += amount
        self.transactions.append(f"Transferido: R$ {amount:.2f} a la cuenta {other_account.id}")
        other_account.transactions.append(f"Recibido: R$ {amount:.2f} de la cuenta {self.id}")
        return f"Transferencia de R$ {amount:.2f} realizada con éxito!"

    def check_balance(self):
        return f"Tu saldo actual es: R$ {self.balance:.2f}"

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def clear_console():
    """Limpia la consola en función del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main_menu():
    print("Bienvenido al Banco Esteban!")
    owner = input("Ingrese su nombre para crear una cuenta: ")
    account = BankAccount(owner)

    accounts_list = [account]  # Esta lista se usa para almacenar las cuentas y poder hacer transferencias

    while True:
        clear_console()
        print("\nMenu:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver extracto")
        print("4. Transferir dinero")
        print("5. Ver saldo")
        print("6. Salir")

        choice = input("\nSeleccione una opción: ")

        if choice == "1":
            amount = input_float("Ingrese la cantidad a depositar: ")
            print(account.deposit(amount))

        elif choice == "2":
            amount = input_float("Ingrese la cantidad a retirar: ")
            print(account.withdraw(amount))
            
        elif choice == "3":
            print(account.get_statement())

        elif choice == "4":
            other_account_id = input("Ingrese el ID de la cuenta a la que desea transferir: ")
            other_account = None

            # Buscar la cuenta usando el ID
            for acc in accounts_list:
                if acc.id == other_account_id:
                    other_account = acc
                    break

            if other_account:
                amount = float(input("Ingrese la cantidad a transferir: "))
                print(account.transfer(other_account, amount))
            else:
                print("Cuenta no encontrada.")

        elif choice == "5":
            print(account.check_balance())

        elif choice == "6":
            print("Gracias por usar nuestro servicio!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

        # Pregunta al usuario si desea regresar al menú principal
        regresar = input("\n¿Desea regresar al menú principal? (s/n): ").lower()
        if regresar != 's':
            break

if __name__ == "__main__":
    main_menu()
