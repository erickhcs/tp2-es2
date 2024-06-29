import unittest
from validate import Validate

fieldNameMock = 'fieldNameTest'

class TestValidate(unittest.TestCase):
  def testEmptyStringError(self):
    with self.assertRaises(ValueError) as context:
      Validate.empty_string(fieldNameMock, '')
    self.assertEqual(str(context.exception), f"{fieldNameMock} parameter should not be empty!")

  def testEmptyStringSuccess(self):
    try:
      Validate.digit(fieldNameMock, 'test')
    except ValueError:
      self.fail("empty_string() raised error unexpectedly!")

  def testDigitError(self):
      with self.assertRaises(ValueError) as context:
        Validate.digit(fieldNameMock, 'test')
      self.assertEqual(str(context.exception), f"{fieldNameMock} parameter should be a number!")
    
  def testDigitSuccess(self):
    try:
      Validate.digit(fieldNameMock, '123')
    except ValueError:
      self.fail("digit() raised error unexpectedly!")
