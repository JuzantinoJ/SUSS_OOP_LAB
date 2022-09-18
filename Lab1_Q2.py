#Q2 - Write a class that models a Rectangle.

class Rectangle:
    def __init__(self, length: float, width:float):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, newLength):
        self._length = newLength

    @property
    def width(self):
        return self._width 

    @width.setter
    def width(self,newWidth):
        self._width = newWidth

   # returns the area of the rectangle 
    def getArea(self):
        return "Area : {{} * {}}".format(self._length,self.width)

    # returns the perimeter of the rectangle 
    def getPerimeter(self):
        return f"Perimeter : {2 * (self._length + self._width)}"

    #increases the length and width of the rectangle by deltaLength and deltaWidth respectively.  
    def IncreaseSize(self,deltaLength, deltaWidth):
        self.length = self._length + deltaLength
        self.width = self._width + deltaWidth
        return f"Increased : {self._length} , {self._width}"

    def __str__(self):
        return 'L : {:.1f} W : {:.1f} A : {:.1f} P : {}'.format(self.length, self.width, self.getArea(), self.getPerimeter())
    #has another rectangle as parameter.
    #returns True if the current area is bigger than the area of the rectangle 
    #rect and False otherwise.
    def isBigger(self,rect):
        if rect.getArea() > self.getArea():
            return True
        else:
            return False 

rect1 = Rectangle(5,20)
rect2 = Rectangle(6,20)

print(rect1.getArea())
print(rect1.getPerimeter())
print(rect1.IncreaseSize(10,10))
print(str(rect1))
print(rect2.getArea())
print(rect2.getPerimeter())
print(rect1.isBigger(rect2))

