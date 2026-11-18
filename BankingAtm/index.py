
import getpass

class BankAccount:
    def __init__(self, account_number, account_holder, PIN, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.PIN = PIN
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount, PIN):
        if PIN == self.PIN and amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def check_balance(self, PIN):
        if PIN == self.PIN:
            return self.balance
        return None

    def display_info(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, PIN, balance, interest_rate, minimum_balance):
        super().__init__(account_number, account_holder, PIN, balance)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount, PIN):
        if PIN == self.PIN and amount > 0 and (self.balance - amount) >= self.minimum_balance:
            self.balance -= amount
            return True
        return False

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, PIN, balance, overdraft_limit):
        super().__init__(account_number, account_holder, PIN, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount, PIN):
        if PIN == self.PIN and amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return True
        return False



class AtmClass:
    def __init__(self):
        self.transactions = []
        self.accounts = [
            SavingsAccount('12345', 'John Doe', '1234', 1000, 2, 500),
            CheckingAccount('67890', 'Jane Doe', '5678', 500, 100)
        ]

    def authenticate(self, account_number, PIN):
        for account in self.accounts:
            if account.account_number == account_number and account.check_balance(PIN) is not None:
                return True
        return False

    def show_menu(self):
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Account Information")
        print("6. Logout")

    def process_transaction(self, account_number, PIN, transaction_type, amount=None):
        if not self.authenticate(account_number, PIN):
            print("Authentication Failed!")
            return False

        for account in self.accounts:
            if account.account_number == account_number:
                if transaction_type == "Check Balance":
                    balance = account.check_balance(PIN)
                    if balance is not None:
                        print(f"Balance: {balance}")
                elif transaction_type == "Deposit":
                    if account.deposit(amount):
                        print("Deposit successful.")
                        self.transactions.append((account_number, "Deposit", amount))
                    else:
                        print("Deposit failed.")
                elif transaction_type == "Withdraw":
                    if account.withdraw(amount, PIN):
                        print("Withdrawal successful.")
                        self.transactions.append((account_number, "Withdrawal", amount))
                    else:
                        print("Withdrawal failed.")
                else:
                    print("Invalid transaction type.")
                return True
        return False

    def display_transactions(self):
        for transaction in self.transactions:
            print(f"Account: {transaction[0]}, Type: {transaction[1]}, Amount: {transaction[2]}")

    def login(self):
        account_number = input("Enter account number: ")
        PIN = getpass.getpass("Enter PIN: ")
        if self.authenticate(account_number, PIN):
            print("Login successful!")
            return account_number
        else:
            print("Invalid account number or PIN.")
            return None


atm = AtmClass()

while True:
    atm.show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        account_type = input("Enter account type (Savings/Checking): ")
        if account_type == 'Savings':
            account_number = atm.login()
            if account_number:
                result = atm.process_transaction(account_number, '1234', 'Check Balance')
        elif account_type == 'Checking':
            account_number = atm.login()
            if account_number:
                result = atm.process_transaction(account_number, '5678', 'Check Balance')
        else:
            print("Invalid account type.")
    elif choice == '2':
        account_type = input("Enter account type (Savings/Checking): ")
        amount = float(input("Enter amount to deposit: "))
        if account_type == 'Savings':
            account_number = atm.login()
            if account_number:
                result = atm.process_transaction(account_number, '1234', 'Deposit', amount)
        elif account_type == 'Checking':
            account_number = atm.login()
            if account_number:
                result = atm.process_transaction(account_number, '5678', 'Deposit', amount)
        else:
            print("Invalid account type.")
    elif choice == '3':
        account_type = input("Enter account type (Savings/Checking): ")
        amount = float(input("Enter amount to withdraw: "))
        if account_type == 'Savings':
            account_number = atm.login()
            if account_number:
                result = atm.process_transaction(account_number, '1234', 'Withdraw', amount)
        elif account_type == 'Checking':
            account_number = atm.login()
            if account_number:
                result = atm.process_transaction(account_number, '5678', 'Withdraw', amount)
        else:
            print("Invalid account type.")
    elif choice == '4':
        atm.display_transactions()
    elif choice == '5':
        pass
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")