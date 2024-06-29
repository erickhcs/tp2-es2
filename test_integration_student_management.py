import unittest
from unittest.mock import patch
from io import StringIO
from student_management import StudentManagement
from db import DB

courseNameMock = "Engenharia de Software 2"
courseIdMock = "DCC072"
courseMaxStudentsMock = "60"

nameMock = "Test"
cpfMock = "123.456.789-01"
registrationMock = "2024092394"

class TestStudentManagement(unittest.TestCase):
  def setUp(self):
    self.cli = StudentManagement()
    self.db = DB()

  def tearDown(self):
    self.db.clear()

  def testAddCourse(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      self.cli.onecmd(f"add_course {courseNameMock};{courseIdMock};{courseMaxStudentsMock}")
      self.assertEqual(fake_out.getvalue().strip(), f"Course {courseNameMock} created with success!")

  def testListCourses(self):
    self.cli.onecmd(f"add_course {courseNameMock};{courseIdMock};{courseMaxStudentsMock}")

    with patch('sys.stdout', new=StringIO()) as fake_out:
      self.cli.onecmd("list_courses")
      self.assertEqual(fake_out.getvalue().strip(), f"Name: {courseNameMock}, ID: {courseIdMock}, Max students: {courseMaxStudentsMock}, Students count: 0")

  def testAddStudent(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      self.cli.onecmd(f"add_student {nameMock};{cpfMock};{registrationMock}")
      self.assertEqual(fake_out.getvalue().strip(), f"Student {nameMock} created with success!")

  def testListStudents(self):
    self.cli.onecmd(f"add_student {nameMock};{cpfMock};{registrationMock}")

    with patch('sys.stdout', new=StringIO()) as fake_out:
      self.cli.onecmd("list_students")
      self.assertEqual(fake_out.getvalue().strip(), f"Name: {nameMock}, CPF: {cpfMock}, Registration: {registrationMock}")

  def testUpdateStudentName(self):
    self.cli.onecmd(f"add_student {nameMock};{cpfMock};{registrationMock}")
    studentNewNameMock = 'New Name Test'

    with patch('sys.stdout', new=StringIO()) as fake_out:
      self.cli.onecmd(f"update_student_name {registrationMock};{studentNewNameMock}")
      self.assertEqual(fake_out.getvalue().strip(), f"Student {studentNewNameMock} has been updated with success!\nStudent with id {registrationMock} name has been updated to {studentNewNameMock} with success!")
