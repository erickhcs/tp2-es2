import cmd
from course import Course
from student import Student
from validate import Validate

CPF_STRING_LENGTH = 14 #xxx.xxx.xxx-xx

class StudentManagement(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to StudentManagement. Type "help" for available commands.'

    def do_quit(self, line):
        'Exit system'
        return True
    
    def do_add_course(self, line):
        'Add a new course separated by semicolon: add_course <name>;<course_id>;<max_students>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 3:
                print("add_course parameters are incorrect. You should pass values separated by semicolon: add_course <name>;<course_id>;<max_students>")
                return
                      
            name=splitted_entry[0]
            course_id=splitted_entry[1]
            max_students=splitted_entry[2]

            Validate.empty_string("name", name)
            Validate.empty_string("course_id", course_id)
            Validate.digit("max_students", max_students)

            newCourse = Course(name,course_id,max_students=int(max_students))
            
            newCourse.create()
        
        except ValueError as e:
            print(f"Error: {e}")

    def do_list_courses(self, line):
        'List all registered courses'
        Course.list_all()
    
    def do_list_students_from_course(self, line):
        'List students from a course: list_students_from_course <course_id>'
        Course.list_course_students(line)

    def do_add_student(self, line):
        'Add a new student separated by semicolon: add_student <name>;<cpf>;<registration>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 3:
                print("add_student parameters are incorrect. You should pass values separated by semicolon: add_student <name>;<cpf>;<registration>")
                return
                      
            name=splitted_entry[0]
            cpf=splitted_entry[1]
            registration=splitted_entry[2]

            Validate.empty_string("name", name)

            if len(cpf) != CPF_STRING_LENGTH:
                print("cpf parameter should be in the format xxx.xxx.xxx-xx!")
                return

            Validate.digit("registration", registration)

            newStudent = Student(name,cpf,registration=int(registration))
            
            newStudent.create()
        
        except ValueError as e:
            print(f"Error: {e}")

    def do_list_students(self, line):
        'List all registered students'
        Student.list_all()

    def do_register_student_in_course(self, line):
        'Register student in course: register_student_in_course <student_registration>;<course_id>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 2:
                print("register_student_in_course parameters are incorrect. You should pass values separated by semicolon: register_student_in_course <student_registration>;<course_id>")
                return
            
            student_registration = splitted_entry[0]
            course_id = splitted_entry[1]

            Validate("course_id", course_id)
            Validate.digit("student_registration", student_registration)
            
            Course.add_student(student_registration=int(student_registration),course_id=course_id)

        except ValueError as e:
            print(f"Error: {e}")

    def do_remove_student_from_course(self, line):
        'Remove student from course: remove_student_from_course <student_registration>;<course_id>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 2:
                    print("remove_student_from_course parameters are incorrect. You should pass values separated by semicolon: remove_student_from_course <student_registration>;<course_id>")
                    return
            
            student_registration = splitted_entry[0]
            course_id = splitted_entry[1]

            Validate.empty_string("course_id",course_id)
            Validate.digit("student_registration", student_registration)
            
            Course.remove_student(student_registration=int(student_registration),course_id=course_id)

        except ValueError as e:
            print(f"Error: {e}")

    def do_update_course_name(self, line):
        'Update course name: update_course_name <course_id>;<course_new_name>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 2:
                print("update_course_name parameters are incorrect. You should pass values separated by semicolon: update_course_name <course_id>;<course_new_name>")
                return
            
            course_id = splitted_entry[0]
            course_new_name = splitted_entry[1]

            Validate.empty_string("course_id", course_id)
            Validate.empty_string("course_new_name", course_new_name)
            
            Course.update_course_name(course_id,course_new_name)
            
        except ValueError as e:
            print(f"Error: {e}")

    def do_update_student_name(self, line):
        'Update student name: do_update_student_name <registration>;<student_new_name>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 2:
                print("do_update_student_name parameters are incorrect. You should pass values separated by semicolon: do_update_student_name <registration>;<student_new_name>")
                return
            
            registration = splitted_entry[0]
            student_new_name = splitted_entry[1]

            Validate.digit("registration", registration)
            Validate.empty_string(fieldName="Student new name", value=student_new_name)
            
            Student.update_student_name(registration=int(registration),student_new_name=student_new_name)
            
        except ValueError as e:
            print(f"Error: {e}")
