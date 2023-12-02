from IncorrectPin import IncorrectPin
from InsufficientFund import InsufficientFund
from InvalidAmount import InvalidAmount


def validate_deposit(amount):
    if amount < 0:
        raise InvalidAmount("Amount is invalid")


class Account:

    def __init__(self, username, number, pin):
        self._username = username
        self._balance = 0
        self._pin = pin
        self._number = number

    def deposit(self, amount: int):
        validate_deposit(amount)
        self._balance += amount

    def check_balance(self, pin: str) -> int:
        self.validate_pin(pin)
        return self._balance

    def withdraw(self, amount, pin: str) -> int:
        self.validate_insufficient_funds(amount)
        self.validate_pin(pin)
        self._pin = pin
        self._balance -= amount

    def getAccountNumber(self):
        return self._number

    def getName(self):
        return self._username

    def validate_pin(self, pin):
        if self._pin != pin:
            raise IncorrectPin("Incorrect pin")

    def validate_insufficient_funds(self,amount):
        if amount > self._balance:
            raise InsufficientFund("Insufficient fund")

