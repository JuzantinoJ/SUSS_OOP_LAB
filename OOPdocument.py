# Encapsulation - keeping whats the use of the function
#eg. using .upper(), dont know whats the function but we use it and know what it does. 

#Creating Class for DICE
from random import randint

class Dice:
    def __init__(self):
        """constructor of dice, random num from 1-6"""
        self._value = randint(1,6)
    
    @property
    def value(self):
        return self.value

    
    def roll(self):
        self._value = randint(1,6)
    
    def __str__(self):
        """ string representation of a Dice object """
        return 'Value: {}'.format(self._value) 

def main():
    d1 = Dice()  # will invoke __init__(d1) 
    count = 0
    while True:
        d1.roll() # roll the dice
        count += 1
        print("Roll {}: {}".format(count,str(d1)))
        if d1.value == 6:
            break
    
main()

# will invoke __init__(d1)
d1 = Dice() 
d2 = Dice()

print(d1.__dict__)
print(d2.__dict__)





#Creating class for CashCard
class CashCard:
    def __init__(self, id: str, amount: float = 100):
        '''Constructor for cashcard, with id and card balance'''
        self._id = id
        self._balance = amount

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        return self._balance

    
        

    # def __str__(self):
    #     """Returns id and balance"""
    #     return f"Id: {self.id} , Balance: {self.balance}"


p1 = CashCard("123")
p2 = CashCard('321')

p2.balance

print(p1.id)
print(p2.balance)