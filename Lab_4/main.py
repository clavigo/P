class Customer:
    def __init__(self, customer_id: int, name: str, address: str, phone_number: str, acct_no: int, bank):
        self.id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.acct_no = acct_no
        self.bank = bank
        self.accounts = []
        self.loans = []

    def general_inquiry(self):
        pass

    def deposit_memory(self):
        pass

    def withdraw_money(self):
        pass

    def open_account(self, teller, account_id: int):
        teller.openAccount(self, account_id)

    def close_account(self, teller, account_id: int):
        teller.closeAccount(self, account_id)

    def apply_for_loan(self, teller, loan_id: int, loan_type: str, account_id: int):
        teller.loanRequest(self, loan_id, loan_type, account_id)

    def request_card(self):
        pass

    def __str__(self):
        return print(f"Bank id = {self.bank.id}, name = {self.bank.name}, location = {self.bank.location},"
                     f"id = {self.id}, name = {self.name}, address = {self.address}, phone_number = {self.phone_number},"
                     f"acct_number = {self.acct_no}]")


class Teller:
    def __init__(self, teller_id: int, name: str, bank):
        self.id = teller_id
        self.name = name
        self.bank = bank

    def collect_money(self):
        pass

    def open_account(self, customer: Customer, account_id: int):
        if account_id not in customer.accounts:
            customer.accounts[account_id] = Account(account_id, customer.id)
            print(f"{account_id} has opened")

    def close_account(self, customer: Customer, account_id: int):
        if account_id in customer.accounts:
            print(f"{account_id} has closed")
            del customer.accounts[account_id]

    def loan_request(self, customer: Customer, loan_id: int, loan_type: str, account_id: int):
        self.openAccount(customer, account_id)
        if loan_id not in customer.loans:
            customer.loans[loan_id] = Loan(loan_id, loan_type, account_id, customer.id)

    def provide_info(self):
        pass

    def issue_card(self):
        pass


class Bank:
    def __init__(self, bank_id: int, name: str, location: str):
        self.id = bank_id
        self.name = name
        self.location = location
        self.tellers = []
        self.customers = []


class Account:
    def __init__(self, account_id: int, customer_id: int):
        self.id = account_id
        self.customer_id = customer_id


class Loan:
    def __init__(self, loan_id: int, type: str, account_id: int, customer_id: int):
        self.id = loan_id
        self.type = type
        self.account_id = account_id
        self.customer_id = customer_id


class Checking(Account):
    def __init__(self, account_id: int, customer_id: int):
        super().__init__(account_id, customer_id)
        self.account_id = account_id
        self.customer_id = customer_id
        if account_id != 0 and customer_id != 0:
            print("Files checked. All good")
        else:
            print("ERROR")


class Savings(Account):
    pass


bank = Bank(1, 'HSBC Bank Plc', 'England')
customer = Customer(customer_id=1, name='Julia', address='3455 Br. Street',
                    phone_number='324-x34-23-664', acct_no=1, bank=bank)

print(f"Customer: {customer.__str__()}")
