import self as self

from Account import Account
from AccountNotFound import AccountNotFound


class Bank:

    def __init__(self):
        self._total_account = 0
        self._accounts = []

    def create_account(self, firstname, lastname, password):
        self._total_account += 1
        name = self.generatename(firstname, lastname)
        account_number = self.generate_account_number()
        account = Account(name, account_number, password)
        self._accounts.append(account)
        return account

    def generatename(self, firstname, lastname):
        return firstname + " " + lastname

    def generate_account_number(self) -> str:
        return str(self._total_account)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def find_account(self, account_number:str):
        for account in self._accounts:
            if account.getAccountNumber() == account_number:
                return account
        else:
            raise AccountNotFound("Account not found")

    def withdraw(self, account_number, pin, amount):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, sender_account_number, sender_pin, receiver_account_number, amount):
        sender_account = self.find_account(sender_account_number)
        receiver_account = self.find_account(receiver_account_number)
        sender_account.withdraw(amount, sender_pin)
        receiver_account.deposit(amount)

    def check_balance(self, account_number, password):
        account = self.find_account(account_number)
        return account.check_balance(password)
