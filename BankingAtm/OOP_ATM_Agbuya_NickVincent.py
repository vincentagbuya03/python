import os
import sys


class BankAccount:
    def __init__(self, NVDA_account_number, NVDA_account_holder, NVDA_pin, NVDA_balance=0.0):
        self._NVDA_account_number = str(NVDA_account_number)
        self._NVDA_account_holder = str(NVDA_account_holder)
        self.__NVDA_pin = str(NVDA_pin)
        self._NVDA_balance = float(NVDA_balance)

    @property
    def NVDA_account_number(self):
        return self._NVDA_account_number

    @property
    def account_number(self):
        return self._NVDA_account_number

    @property
    def NVDA_account_holder(self):
        return self._NVDA_account_holder

    @property
    def account_holder(self):
        return self._NVDA_account_holder

    @property
    def NVDA_balance(self):
        return self._NVDA_balance

    @property
    def balance(self):
        return self._NVDA_balance

    @property
    def NVDA_account_type(self):
        return "Standard Account"

    @property
    def account_type(self):
        return self.NVDA_account_type

    def verify_pin(self, NVDA_entered_pin):
        return self.__NVDA_pin == str(NVDA_entered_pin)

    def check_balance(self):
        print("----------------- BALANCE INQUIRY -----------------")
        print(f"Account Holder: {self._NVDA_account_holder}")
        print(f"Current Balance: PHP {self._NVDA_balance:,.2f}")
        return self._NVDA_balance

    def deposit(self, NVDA_amount):
        if NVDA_amount > 0:
            self._NVDA_balance += NVDA_amount
            return True
        return False

    def withdraw(self, NVDA_amount):
        if NVDA_amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if NVDA_amount > self._NVDA_balance:
            return False, "Insufficient balance!"
        self._NVDA_balance -= NVDA_amount
        return True, "Withdrawal Successful!"

    def display_info(self):
        print(f"Account Number : {self._NVDA_account_number}")
        print(f"Account Holder : {self._NVDA_account_holder}")
        print(f"Account Type   : {self.account_type}")
        print(f"Current Balance: PHP {self._NVDA_balance:,.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, NVDA_account_number, NVDA_account_holder, NVDA_pin, NVDA_balance, NVDA_minimum_balance=500.0):
        super().__init__(NVDA_account_number, NVDA_account_holder, NVDA_pin, NVDA_balance)
        self._NVDA_minimum_balance = float(NVDA_minimum_balance)

    @property
    def NVDA_minimum_balance(self):
        return self._NVDA_minimum_balance

    @property
    def minimum_balance(self):
        return self._NVDA_minimum_balance

    @property
    def NVDA_account_type(self):
        return "Savings Account"

    @property
    def account_type(self):
        return self.NVDA_account_type

    def withdraw(self, NVDA_amount):
        if NVDA_amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if (self._NVDA_balance - NVDA_amount) < self._NVDA_minimum_balance:
            return False, "Insufficient balance!"
        self._NVDA_balance -= NVDA_amount
        return True, "Withdrawal Successful!"

    def display_info(self):
        super().display_info()
        print(f"Minimum Balance: PHP {self._NVDA_minimum_balance:,.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, NVDA_account_number, NVDA_account_holder, NVDA_pin, NVDA_balance, NVDA_overdraft_limit=1000.0):
        super().__init__(NVDA_account_number, NVDA_account_holder, NVDA_pin, NVDA_balance)
        self._NVDA_overdraft_limit = float(NVDA_overdraft_limit)

    @property
    def NVDA_overdraft_limit(self):
        return self._NVDA_overdraft_limit

    @property
    def overdraft_limit(self):
        return self._NVDA_overdraft_limit

    @property
    def NVDA_account_type(self):
        return "Checking Account"

    @property
    def account_type(self):
        return self.NVDA_account_type

    def withdraw(self, NVDA_amount):
        if NVDA_amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if (self._NVDA_balance - NVDA_amount) < -self._NVDA_overdraft_limit:
            return False, "Insufficient balance!"
        self._NVDA_balance -= NVDA_amount
        return True, "Withdrawal Successful!"

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: PHP {self._NVDA_overdraft_limit:,.2f}")


class ATM:
    def __init__(self):
        self.NVDA_accounts = [
            SavingsAccount("100001", "Juan Dela Cruz", "1234", 10000.0, NVDA_minimum_balance=500.0),
            CheckingAccount("100002", "Maria Santos", "5678", 15000.0, NVDA_overdraft_limit=1000.0)
        ]
        self.NVDA_transactions = []
        self.accounts = self.NVDA_accounts
        self.transactions = self.NVDA_transactions

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_masked_pin(self, NVDA_prompt="Enter PIN: "):
        sys.stdout.write(NVDA_prompt)
        sys.stdout.flush()
        NVDA_pin = ""
        try:
            import msvcrt
            while True:
                NVDA_ch = msvcrt.getch()
                if NVDA_ch in (b"\r", b"\n"):
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                    break
                elif NVDA_ch in (b"\x08", b"\x7f"):
                    if len(NVDA_pin) > 0:
                        NVDA_pin = NVDA_pin[:-1]
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()
                elif NVDA_ch == b"\x03":
                    raise KeyboardInterrupt
                else:
                    NVDA_char = NVDA_ch.decode("utf-8", errors="ignore")
                    if NVDA_char.isprintable():
                        NVDA_pin += NVDA_char
                        sys.stdout.write("*")
                        sys.stdout.flush()
        except ImportError:
            try:
                import termios
                import tty
                NVDA_fd = sys.stdin.fileno()
                NVDA_old_settings = termios.tcgetattr(NVDA_fd)
                try:
                    tty.setraw(NVDA_fd)
                    while True:
                        NVDA_ch = sys.stdin.read(1)
                        if NVDA_ch in ("\r", "\n"):
                            sys.stdout.write("\r\n")
                            sys.stdout.flush()
                            break
                        elif NVDA_ch in ("\x08", "\x7f"):
                            if len(NVDA_pin) > 0:
                                NVDA_pin = NVDA_pin[:-1]
                                sys.stdout.write("\b \b")
                                sys.stdout.flush()
                        elif NVDA_ch == "\x03":
                            raise KeyboardInterrupt
                        elif NVDA_ch.isprintable():
                            NVDA_pin += NVDA_ch
                            sys.stdout.write("*")
                            sys.stdout.flush()
                finally:
                    termios.tcsetattr(NVDA_fd, termios.TCSADRAIN, NVDA_old_settings)
            except Exception:
                NVDA_pin = input()
        return NVDA_pin

    def find_account(self, NVDA_account_number):
        for NVDA_account in self.NVDA_accounts:
            if NVDA_account.account_number == str(NVDA_account_number):
                return NVDA_account
        return None

    def authenticate(self, NVDA_account_number, NVDA_pin):
        NVDA_account = self.find_account(NVDA_account_number)
        if NVDA_account and NVDA_account.verify_pin(NVDA_pin):
            return NVDA_account
        return None

    def show_menu(self):
        print("==============================")
        print("      BANKING ATM SYSTEM      ")
        print("------------------------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Account Information")
        print("6. Logout")
        print("------------------------------")

    def display_transactions(self, NVDA_account_number):
        print("----------------- TRANSACTION HISTORY -----------------")
        NVDA_user_txs = [NVDA_tx for NVDA_tx in self.NVDA_transactions if NVDA_tx["account_number"] == NVDA_account_number]
        if not NVDA_user_txs:
            print("No transactions recorded.")
        else:
            for NVDA_idx, NVDA_tx in enumerate(NVDA_user_txs, 1):
                print(f"{NVDA_idx}. {NVDA_tx['record']}")
        print("-------------------------------------------------------")
        print(f"Total Transactions: {len(NVDA_user_txs)}")

    def process_transaction(self, NVDA_account, NVDA_choice):
        if NVDA_choice == '1':
            NVDA_account.check_balance()

        elif NVDA_choice == '2':
            print("----------------- CASH DEPOSIT -----------------")
            try:
                NVDA_amount_input = input("Enter Amount to Deposit: PHP ").strip()
                NVDA_amount = float(NVDA_amount_input)
                if NVDA_amount <= 0:
                    print("ERROR: Deposit amount must be greater than zero.")
                    return

                NVDA_prev_balance = NVDA_account.balance
                if NVDA_account.deposit(NVDA_amount):
                    print("Deposit Successful!")
                    print(f"Previous Balance: PHP {NVDA_prev_balance:,.2f}")
                    print(f"Deposited Amount: PHP {NVDA_amount:,.2f}")
                    print(f"New Balance: PHP {NVDA_account.balance:,.2f}")
                    self.NVDA_transactions.append({
                        "account_number": NVDA_account.account_number,
                        "record": f"Deposit PHP {NVDA_amount:,.2f}"
                    })
            except ValueError:
                print("ERROR: Invalid amount! Please enter a valid number.")

        elif NVDA_choice == '3':
            print("----------------- CASH WITHDRAWAL -----------------")
            try:
                NVDA_amount_input = input("Enter Amount to Withdraw: PHP ").strip()
                NVDA_amount = float(NVDA_amount_input)
                if NVDA_amount <= 0:
                    print("ERROR: Withdrawal amount must be greater than zero.")
                    return

                NVDA_prev_balance = NVDA_account.balance
                NVDA_success, NVDA_message = NVDA_account.withdraw(NVDA_amount)
                if NVDA_success:
                    print("Withdrawal Successful!")
                    print(f"Previous Balance: PHP {NVDA_prev_balance:,.2f}")
                    print(f"Withdrawn Amount: PHP {NVDA_amount:,.2f}")
                    print(f"Remaining Balance: PHP {NVDA_account.balance:,.2f}")
                    self.NVDA_transactions.append({
                        "account_number": NVDA_account.account_number,
                        "record": f"Withdrawal PHP {NVDA_amount:,.2f}"
                    })
                else:
                    print(f"ERROR: {NVDA_message}")
                    print(f"Available Balance: PHP {NVDA_account.balance:,.2f}")
                    print("Transaction cancelled.")
            except ValueError:
                print("ERROR: Invalid amount! Please enter a valid number.")

        elif NVDA_choice == '4':
            self.display_transactions(NVDA_account.account_number)

        elif NVDA_choice == '5':
            print("----------------- ACCOUNT INFORMATION -----------------")
            NVDA_account.display_info()
            print("-------------------------------------------------------")

    def login(self):
        NVDA_max_attempts = 3
        NVDA_attempts = 0

        self.clear_screen()
        print("==============================")
        print("      BANKING ATM SYSTEM      ")
        print("==============================")

        while NVDA_attempts < NVDA_max_attempts:
            try:
                NVDA_account_number = input("Enter Account Number: ").strip()
                if not NVDA_account_number:
                    print("ERROR: Account number cannot be empty.\n")
                    continue

                NVDA_pin = self.get_masked_pin("Enter PIN: ").strip()
                if not NVDA_pin:
                    print("ERROR: PIN cannot be empty.\n")
                    continue

                NVDA_account = self.authenticate(NVDA_account_number, NVDA_pin)
                if NVDA_account:
                    print("Login Successful!")
                    print(f"Welcome, {NVDA_account.account_holder}")
                    print(f"Account Type: {NVDA_account.account_type}")
                    input("\nPress Enter to continue to Main Menu...")
                    self.clear_screen()
                    return NVDA_account
                else:
                    NVDA_attempts += 1
                    NVDA_remaining = NVDA_max_attempts - NVDA_attempts
                    NVDA_existing = self.find_account(NVDA_account_number)
                    if not NVDA_existing:
                        print("ERROR: Account not found!")
                    else:
                        print("ERROR: Incorrect PIN!")

                    if NVDA_remaining > 0:
                        print(f"Remaining Attempts: {NVDA_remaining}\n")
                    else:
                        print("ERROR: Maximum login attempts exceeded. Access locked.\n")
                        return None
            except (KeyboardInterrupt, EOFError):
                print("\nLogin cancelled.")
                return None
        return None

    def run(self):
        NVDA_account = self.login()
        if not NVDA_account:
            return

        while True:
            try:
                self.clear_screen()
                self.show_menu()
                NVDA_choice = input("Enter your choice: ").strip()

                if NVDA_choice in ['1', '2', '3', '4', '5']:
                    self.clear_screen()
                    self.process_transaction(NVDA_account, NVDA_choice)
                    input("\nPress Enter to continue...")
                elif NVDA_choice == '6':
                    self.clear_screen()
                    print(f"Thank you for banking with us, {NVDA_account.account_holder}!")
                    print("Logout successful. Goodbye!\n")
                    break
                else:
                    input("\nERROR: Invalid choice! Please enter a number from 1 to 6.\nPress Enter to continue...")
            except (KeyboardInterrupt, EOFError):
                print(f"\nSession terminated. Goodbye, {NVDA_account.account_holder}!")
                break


AtmClass = ATM

if __name__ == "__main__":
    NVDA_atm = ATM()
    NVDA_atm.run()
