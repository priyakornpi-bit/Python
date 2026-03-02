class BankAccount:
    # ===== Class Variables =====
    branch = "5511"
    running_saving = 0
    running_loan = 0

    def __init__(self, name, account_type="saving"):
        # ===== Instance Variables =====
        self.name = name
        self.account_type = account_type
        self.balance = 0

        # ===== Generate account number =====
        if account_type == "saving":
            BankAccount.running_saving += 1
            running = BankAccount.running_saving
            type_code = 1
        elif account_type == "loan":
            BankAccount.running_loan += 1
            running = BankAccount.running_loan
            type_code = 2
        else:
            raise ValueError("Invalid account type")

        self.account_number = f"{BankAccount.branch}-{type_code}-{running}"

    def print_customer(self):
        print("----- Customer Record -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Account type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print("----- End Record -----")

    def deposit(self, amount):
        self.balance += amount

# Create accounts
john = BankAccount("John", "saving")
tim = BankAccount("Tim", "loan")
sarah = BankAccount("Sarah", "saving")

# Initial amounts
john.deposit(500)
tim.deposit(-1_000_000)
sarah.deposit(50_000_000)

accounts = [john, tim, sarah, sarah_loan]

for acc in accounts:
    acc.print_customer()
