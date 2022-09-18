#Q3.  Write a class Point that models a 2 dimensional point (x,y). 

class Point:
    def __init__(self, x:float = 0, y:float= 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} , {self.y}"

    #getter method x
    def x(self):
        return self.x
    #getter method y
    def y(self):
        return self.y

    #setter method x
    def x(self,x:float):
        self.x = x

    def y(self,y:float):
        self.y = y

    #moves dx,dy
    def move(self,dx,dy):
        return self.x + dx , self.y + dy

    #returns dist to another point (x1,y1) 
    def distanceTo(self,aPoint):
        dist = (self)

        return dist

test = Point(5,4)

test.x = 10
test.y = 50
print(test)