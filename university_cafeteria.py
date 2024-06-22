class UniversityCafeteria:
    def __init__(self, meal_price=4.0):
        self.meal_price = meal_price

    def pay_meal(self, student):
        if student.credit.debit_credit(self.meal_price):
            print("Meal paid successfully.")
        else:
            print("Meal payment failed.")
