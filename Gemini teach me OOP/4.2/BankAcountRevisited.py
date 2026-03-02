class BankAccount:
    branch_name = "5511" # class attribute: shared by all accounts
    def __init__(self, name, account_type="saving"):
        # AI-assisted explanation:
        # This constructor initializes basic account information.
        # I understand how name, account_type, and balance are stored.
        self.name = name 
        self.account_type = account_type
        self.balance = 0

         
    @classmethod
    def change_branch_name(cls, new_name):
        # AI-assisted explanation:
        # This class method updates the branch name for all BankAccount objects.
        cls.branch_name = new_name

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if self.account_type != "saving":
            print("Withdraw is allowed only for saving account")
            return 
        self.balance -= amount

    def pay_loan(self,amount):
        if self.account_type != "loan":
            print("loan is allowed to play for loan account")
            return
        self.balance += amount

    def get_loan(self,amount):
       # AI-assisted explanation:
    # This method allows getting more loan under specific conditions.

        if self.account_type != "loan":
            return "Get loan is allowed only for loan account"

        if self.balance < -50000:
            return "Loan limit exceeded"
        self.balance -= amount

    @staticmethod
    def calc_interest(balance, int_rate, payment):
        year_count = 1
        while balance > 0:
            interest = balance * int_rate / 100
            new_bal = balance + interest
            balance = new_bal - payment
            pass
    
    

