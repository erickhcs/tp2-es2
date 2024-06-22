class Aid:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"Aid: {self.type}, Amount: ${self.amount:.2f}"
