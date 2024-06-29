import unittest
from unittest.mock import patch
from io import StringIO
from student import Student

nameMock = "Test"
cpfMock = "123.456.789-01"
registrationMock = "2024092394"
aidValueMock = 5

class TestStudent(unittest.TestCase):
  def setUp(self):
    self.student = Student(nameMock,cpfMock,registrationMock)
  
  def testStudentInit(self):
    self.assertEqual(self.student.name,nameMock)
    self.assertEqual(self.student.cpf,cpfMock)
    self.assertEqual(self.student.registration,registrationMock)
    self.assertEqual(self.student.aids,[])

  def testStudentString(self):
    self.assertEqual(str(self.student), f"Student: {nameMock}, CPF: {cpfMock}, Registration: {registrationMock}, Credit: ${self.student.credit.balance:.2f}")

  @patch('sys.stdout', new_callable=StringIO)
  def testShowAidsError(self, mock_stdout):
    self.student.show_aids()

    self.assertEqual(mock_stdout.getvalue(), f"{nameMock} has no aids.\n")

  @patch('sys.stdout', new_callable=StringIO)
  def testShowBalance(self, mock_stdout):
    self.student.show_balance()

    self.assertEqual(mock_stdout.getvalue(), f"Current balance of {nameMock}: ${self.student.credit.balance:.2f}\n")
