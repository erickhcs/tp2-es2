import unittest
from unittest.mock import patch
from io import StringIO
from credit import Credit

creditBalanceMock = 50

class TestCredit(unittest.TestCase):
  def setUp(self):
    self.credit = Credit(creditBalanceMock)
  
  def testCreditInit(self):
    self.assertEqual(self.credit.balance, creditBalanceMock)

  @patch('sys.stdout', new_callable=StringIO)
  def testAddCredit(self, mock_stdout):
    amount = 100
    self.credit.add_credit(amount)

    self.assertEqual(self.credit.balance, creditBalanceMock + amount)
    self.assertEqual(mock_stdout.getvalue(), f"Credit of ${amount:.2f} added. Current balance: ${self.credit.balance:.2f}\n")

  @patch('sys.stdout', new_callable=StringIO)
  def testAddCreditError(self, mock_stdout):
    amount = -100
    self.credit.add_credit(amount)

    self.assertEqual(self.credit.balance, creditBalanceMock)
    self.assertEqual(mock_stdout.getvalue(), "Cannot add negative credit!\n")

  @patch('sys.stdout', new_callable=StringIO)
  def testDebitCredit(self, mock_stdout):
    amount = 10

    self.assertEqual(self.credit.debit_credit(amount), True)
    self.assertEqual(self.credit.balance, creditBalanceMock - amount)
    self.assertEqual(mock_stdout.getvalue(), f"${amount:.2f} debited. Current balance: ${self.credit.balance:.2f}\n")

  @patch('sys.stdout', new_callable=StringIO)
  def testDebitCreditError(self, mock_stdout):
    amount = 60

    self.assertEqual(self.credit.debit_credit(amount), False)
    self.assertEqual(self.credit.balance, creditBalanceMock)
    self.assertEqual(mock_stdout.getvalue(), "Insufficient balance.\n")
