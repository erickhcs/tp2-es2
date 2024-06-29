import unittest
from aid import Aid

aidTypeMock = "test"
aidAmountMock = 50

class TestAid(unittest.TestCase):
  def setUp(self):
    self.aid = Aid(aidTypeMock, aidAmountMock)

  def testAidInit(self):
    self.assertEqual(self.aid.type, aidTypeMock)
    self.assertEqual(self.aid.amount, aidAmountMock)
  
  def testAidString(self):
    self.assertEqual(str(self.aid), f"Aid: {aidTypeMock}, Amount: ${aidAmountMock:.2f}")
