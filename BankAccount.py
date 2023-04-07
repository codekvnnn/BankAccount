class BankAccount:
    def __init__(self, account_number, date, balance, customer_name): 
        self.no = account_number
        self.date = date
        self.balance = balance
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
    
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
        
    def display_account_info(self):
        self.no = self
        print(f"Current balance is ${self.account}.")
        
    def yield_interest(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date)
        print(f"Balance: ${self.balance}\n")
        
# Input customer details
ac_no_1 = BankAccount(2345, "01-01-2011", 1000, "Toninho Takeo")
ac_no_2 = BankAccount(1234, "11-03-2011", 2000, "Astrid Rugile")
ac_no_3 = BankAccount(2312, "12-01-2009", 3000, "Orli Kerenza")
ac_no_4 = BankAccount(1395, "01-01-2011", 3000, "Luciana Chika")
ac_no_5 = BankAccount(6345, "01-05-2011", 4000, "Toninho Takeo")

print("Customer Details:")
ac_no_1.yield_interest()
ac_no_2.yield_interest()
ac_no_3.yield_interest()
ac_no_4.yield_interest()
ac_no_5.yield_interest()
