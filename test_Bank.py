from unittest import TestCase

from Bank import Bank


class TestBank(TestCase):
    def test_i_create_account(self):
        bank = Bank()
        account = bank.create_account("Delighted", "Adewuyi", "password")
        self.assertEqual("1", bank.generate_account_number())
        self.assertEqual("1", account.getAccountNumber())

    def test_that_when_bank_created_two_account_if_can_find_both(self):
        bank = Bank()
        account1 = bank.create_account("Delighted", "Adewuyi", "password")
        account2 = bank.create_account("ope", "Ogungbeni", "opePassword")
        self.assertEqual(account1, bank.find_account("1"))
        self.assertEqual(account2, bank.find_account("2"))

    def test_that_bank_user_can_deposit_to_their_account(self):
        bank = Bank()
        account1 = bank.create_account("Delighted", "Adewuyi", "password")
        bank.deposit("1", 2000)
        self.assertEqual(2000, bank.check_balance("1","password"))

    def test_that_bank_user_can_deposit_multiple_times(self):
        bank = Bank()
        account1 = bank.create_account("Delighted", "Adewuyi", "password")
        bank.deposit("1",2000)
        bank.deposit("1",3000)
        bank.deposit("1",5000)
        self.assertEqual(10_000,bank.check_balance("1","password"))

    def test_that_bank_user_can_withdraw_when_user_deposit(self):
        bank = Bank()
        account1 = bank.create_account("Delighted", "Adewuyi", "password")
        bank.deposit("1", 2000)
        bank.deposit("1", 3000)
        self.assertEqual(5_000, bank.check_balance("1","password"))
        bank.withdraw("1","password",2500)
        self.assertEqual(2_500,bank.check_balance("1","password"))

    def test_that_bank_user_can_transfer_to_another_bank_user(self):
        bank = Bank()
        bank.create_account("Delighted", "Adewuyi", "password")
        bank.deposit("1",6000)
        bank.create_account("ope", "Ogungbeni", "opePassword")
        bank.transfer("1","password","2",5000)
        self.assertEqual(1000,bank.check_balance("1","password"))
        self.assertEqual(5000,bank.check_balance("2","opePassword"))






