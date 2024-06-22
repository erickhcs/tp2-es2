from db import DB
from credit import Credit

class Student:
    def __init__(self, name, cpf, registration):
        self.name = name
        self.cpf = cpf
        self.registration = registration
        self.credit = Credit(balance=0.0)
        self.aids = []

    def __str__(self):
        return f"Student: {self.name}, CPF: {self.cpf}, Registration: {self.registration}, Credit: ${self.credit.balance:.2f}"

    def add_aid(self, aid):
        self.credit.add_credit(aid.amount)
        self.aids.append(aid)
        print(f"Aid {aid.type} of ${aid.amount:.2f} added to student {self.name}.")

    def show_aids(self):
        if not self.aids:
            print(f"{self.name} has no aids.")
        else:
            print(f"Aids of {self.name}:")
            for aid in self.aids:
                print(f" - {aid}")

    def show_balance(self):
        print(f"Current balance of {self.name}: ${self.credit.balance:.2f}")
    
    def create(self):
        db = DB()

        studentInDB = db.get(tableName="students", field="registration", data=self.registration)

        if (studentInDB):
            print(f"Student with registration {self.registration} already exists!")
            return

        db.insert(tableName="students", data={'registration': self.registration, 'name': self.name, 'cpf': self.cpf, 'aids': self.aids, 'credit': self.credit.balance})

        print(f"Student {self.name} created with success!")

    def update(self):
        db = DB()

        studentInDB = db.get(tableName="students", field="registration", data=self.registration)

        if not studentInDB:
            print(f"Student with id {self.registration} doesn't exists!")
            return
        
        db.update(tableName="students",field="registration",fieldData=self.registration,data={'registration': self.registration, 'name': self.name, 'cpf': self.cpf, 'aids': self.aids, 'credit': self.credit.balance})

        print(f"Student {self.name} has been updated with success!")

    @staticmethod
    def get(student_registration):
        db = DB()

        return db.get(tableName="students",field="registration",data=student_registration)

    @staticmethod
    def list_all():
        db = DB()

        all_students = db.get_all(tableName="students")

        for student in all_students:
            name = student["name"]
            cpf = student["cpf"]
            registration = student["registration"]

            print(f"Name: {name}, CPF: {cpf}, Registration: {registration}")

    @staticmethod
    def get_all():
        db = DB()

        all_students = db.get_all(tableName="students")

        return all_students
    
    @staticmethod
    def update_student_name(registration,student_new_name):
        db = DB()

        student = db.get(tableName="students",field="registration",data=registration)

        if not student:
            print(f"Student registration {registration} doesn't exists!")
            return
        
        studentObj = Student(name=student_new_name,cpf=student['cpf'],registration=student['registration'])
        studentObj.credit = Credit(balance=student['credit'])
        studentObj.aids = student['aids']
        studentObj.update()

        print(f"Student with id {student['registration']} name has been updated to {student_new_name} with success!")
