class BankAccount:
    amount = 100
    def __init__(self):
        self.balance = 0
        self.open_account = False
        
    def get_balance(self):
        if self.open_account:
            return self.balance
            raise_error('Account closed')

    def open(self):
        self.open_account = True

    def deposit(self, amount):
        if self.open_account:
            if amount > 0:
                self.balance += amount
                return self.balance

    def withdraw(self, amount):
        if self.open_account:
            if amount <= self.balance:
                if amount > 0:
                    self.balance -= amount
                    return self.balance
                raise_error('Can not withdraw negative amount')
            raise_error('Insufficient balance')
        raise_error('Account is closed')
    
    def close(self):
        self.open_account = False
