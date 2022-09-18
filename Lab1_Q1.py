#Q1 -  Write a class Person that models a person’s particulars as shown in the UML 
# diagram: 

class Person:
    def __init__(self, gender:str, name:str, lastName:str) :
        self._gender = gender
        self._name = name
        self._lastName = lastName

    @property #accessor method
    def gender(self):
        return self._gender

    @property  #accessor method
    def name(self):
        return self._name

    @name.setter 
    def name(self,newName):
        self._name = newName

    @property  #accessor method
    def lastName(self):
        return self._lastName

    def __str__(self):
        return f"Name: {self._name} | Gender: {self._gender}"


    # return the last name, followed by the name,
    def getFullName(self):
        """
        This is to get full name , firstname and lastname
        """
        if self._gender[0] in "mM":
            return f"Mr. {self._lastName} {self._name}"
        elif self._gender[0] in 'fF':
            return f"Ms. {self._lastName} {self._name}"

    #returns the first letter of the name separated by blanks, followed by the lastname.
    def getInitials(self):
        """return the first letter of the name, followed by lastname"""
        return f"{self._name[0]}. {self._lastName}"


Tino = Person('male', 'Juzantino', 'Junadi')
print(str(Tino))
print(Tino.getFullName())
print(Tino.getInitials())
print(Tino)

