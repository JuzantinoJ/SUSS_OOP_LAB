#Q4.  Write a BankAccount class that models a Bank Account.

class BankAccount:
    def __init__(self, accountId:str , pin: int, amount:float):
        self._accountId = accountId
        self._pin = pin
        self._balance = amount

    #getter for accountId
    @property
    def accountId(self):
        return self._accountId

    #getter for pin
    @property
    def pin(self):
        return self._pin

    #getter for balance
    @property
    def balance(self):
        return self._balance

    #setter for balance
    @balance.setter
    def balance(self, newBalance):
        self._balance = newBalance

    # changePin method
    def changePin(self,oldPin ,newPin):
        """Change of pin is updated 
        only if the old pin matches 
        the existing pin """
        if self._pin == oldPin:
            self._pin = newPin
            return True
        else:
            return False


    #deposit method
    def deposit(self, amount):
        """
        A deposit method with parameter amount which represents the amount to 
        deposit. The method adds the amount to the balance.
        """
        if amount > 0:
            self._balance += amount
            
    #withdraw method
    def withdraw(self,amount):
        """
        A withdraw method with parameter amount which represents the withdrawal 
        amount. This method deducts the amount from the balance and returns True 
        if there is sufficient balance, and False otherwise.
        """
        if amount < self._balance:
            newAmount = self._balance - amount
            self.balance = newAmount
            return True
        else:
            return False


    #transfer method
    def transfer(self, acct, amount):
        '''method to transfer amount between account objects'''
        if self.withdraw(amount):
            acct.deposit(amount)
            return True
            
        return False
        

    def __str__(self):
        return f"{self._accountId} , {self._pin} , {self._balance}"

# tino = BankAccount('001', 888888, 100)
# kyer = BankAccount('002', 444444, 300)

def main():
    b1 = BankAccount('B1', 111 , 100)
    b1.deposit(100)
    print(b1)
    b1.changePin(111,222)
    print(b1)
    b2 = BankAccount('B2',222, 100)
    print(b2.withdraw(200))
    print(b1.transfer(b2,100))
    print(b1.balance)
    print(b2.balance)
main()
