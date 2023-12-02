from unittest import TestCase
from Account import Account
from IncorrectPin import IncorrectPin
from InsufficientFund import InsufficientFund
from InvalidAmount import InvalidAmount


class TestAccount(TestCase):
    def test_that_account_can_deposit_1k_and_check_balance_would_be_1k(self):
        my_account = Account("Delighted", "1", "password")
        my_account.deposit(500)
        self.assertEqual(500, my_account.check_balance("password"))

    def test_that_if_amount_deposited_is_less_zero_balance_wont_change(self):
        with self.assertRaises(InvalidAmount):
            my_account = Account("Delighted", "1", "password")
            my_account.deposit(-200)
            self.assertEqual(0, my_account.check_balance("password"))

    def test_balance_wont_be_check_if_pin_is_incorrect(self):
        with self.assertRaises(IncorrectPin):
            my_account = Account("Delighted", "1", "password")
            my_account.deposit(2_000)
            self.assertEqual(2_000, my_account.check_balance("incorrect_Password"))

    def test_that_when_i_deposit_2_5k_if_i_withdraw_1k_balance_would_be_1_5k(self):
        my_account = Account("Delighted", "1", "password")
        my_account.deposit(2500)
        my_account.withdraw(1000, "password")
        self.assertEqual(1500, my_account.check_balance("password"))

    def test_if_i_deposit_3000_and_try_to_withdraw_3500_my_balance_wont_change(self):
        with self.assertRaises(InsufficientFund):
            my_account = Account("Delighted", "1", "password")
            my_account.deposit(3000)
            my_account.withdraw(3500, "password")
            self.assertEqual(3000, my_account.check_balance("password"))

    def test_if_i_deposit_2000_and_try_to_withdraw_1000_with_incorrect_password_my_balance_wont_change(self):
        with self.assertRaises(IncorrectPin):
            my_account = Account("Delighted", "1", "password")
            my_account.deposit(2_000)
            my_account.withdraw(1_00, "password")
            self.assertEqual(2_000, my_account.check_balance("incorrect_password"))
