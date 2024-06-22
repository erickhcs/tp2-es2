class Credit:
    def __init__(self, balance):
        self.balance = balance

    def add_credit(self, amount):
        self.balance += amount
        print(f"Credit of ${amount:.2f} added. Current balance: ${self.balance:.2f}")

    def debit_credit(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        print(f"${amount:.2f} debited. Current balance: ${self.balance:.2f}")
        return True
