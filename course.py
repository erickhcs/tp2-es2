from db import DB
from student import Student

class Course:
    def __init__(self, name, course_id, max_students):
        self.name = name
        self.id = course_id
        self.max_students = max_students
        self.students = []

    def create(self):
        db = DB()

        courseInDB = db.get(tableName="courses", field="id", data=self.id)

        if (courseInDB):
            print(f"Course with id {self.id} already exists!")
            return

        db.insert(tableName="courses", data={'id': self.id, 'name': self.name, 'max_students': self.max_students, 'students': self.students})

        print(f"Course {self.name} created with success!")

    def update(self):
        db = DB()

        courseInDB = db.get(tableName="courses", field="id", data=self.id)

        if not courseInDB:
            print(f"Course with id {self.id} doesn't exists!")
            return
        
        db.update(tableName="courses",field="id",fieldData=self.id,data={'id': self.id, 'name': self.name, 'max_students': self.max_students, 'students': self.students})

        print(f"Course {self.name} has been updated with success!")

    @staticmethod
    def list_all():
        db = DB()

        all_courses = db.get_all(tableName="courses")

        for course in all_courses:
            name = course["name"]
            course_id = course["id"]
            max_students = course["max_students"]
            students_count = len(course["students"])

            print(f"Name: {name}, ID: {course_id}, Max students: {max_students}, Students count: {students_count}")
    
    @staticmethod
    def list_course_students(course_id):
        db = DB()

        course = db.get(tableName="courses",field="id",data=course_id)

        if not course:
            print(f"Course id {course_id} doesn't exists!")
            return
        
        all_students = Student.get_all()

        students_in_course = list(filter(lambda student: student['registration'] in set(course['students']), list(all_students)))

        if not students_in_course:
            print(f"Students list from course {course['name']} is empty!")
            return

        for student in students_in_course:
            name = student["name"]
            cpf = student["cpf"]
            registration = student["registration"]

            print(f"Name: {name}, CPF: {cpf}, Registration: {registration}")
    
    @staticmethod
    def add_student(student_registration,course_id):
        db = DB()

        course = db.get(tableName="courses",field="id",data=course_id)
        student = Student.get(student_registration)

        if not course:
            print(f"Course id {course_id} doesn't exists!")
            return

        if not student:
            print(f"Student registration {student_registration} doesn't exists!")
            return
        
        if student['registration'] in set(course['students']):
            print(f"Student {student['name']} is already registered in the course {course['name']}!")
            return
                
        if len(course['students']) >= course['max_students']:
            print(f"Course {course['name']} is already full!")
            return
        
        courseObj = Course(name=course['name'],course_id=course['id'],max_students=course['max_students'])
        courseObj.students = course['students'] + [student['registration']]

        courseObj.update()

        print(f"Student {student['name']} has been registered to the course {course['name']} with success!")

    @staticmethod
    def remove_student(student_registration,course_id):
        db = DB()

        course = db.get(tableName="courses",field="id",data=course_id)
        student = Student.get(student_registration)

        if not course:
            print(f"Course id {course_id} doesn't exists!")
            return

        if not student:
            print(f"Student registration {student_registration} doesn't exists!")
            return
        
        if not student['registration'] in set(course['students']):
            print(f"Student {student['name']} is not registered in the course {course['name']}!")
            return
                
        courseObj = Course(name=course['name'],course_id=course['id'],max_students=course['max_students'])

        new_students_in_course = list(filter(lambda registeredStudentRegistration: registeredStudentRegistration != student[ 'registration'], list(course['students'])))

        courseObj.students = new_students_in_course

        courseObj.update()

        print(f"Student {student['name']} has been removed from the course {course['name']} with success!")
    
    @staticmethod
    def update_course_name(course_id,new_course_name):
        db = DB()

        course = db.get(tableName="courses",field="id",data=course_id)

        if not course:
            print(f"Course id {course_id} doesn't exists!")
            return
        
        courseObj = Course(name=new_course_name,course_id=course['id'],max_students=course['max_students'])
        courseObj.students = course['students']
        courseObj.update()

        print(f"Course with id {course['id']} name has been updated to {new_course_name} with success!")
