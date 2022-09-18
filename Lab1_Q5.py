# Write a ToDo class that allows a user to record things to do for an event, e.g.    
# travelling trip.

class ToDo:
    def __init__(self,event: str ):
        self._event = event
        self._actions = []
       

    #getter for event name
    @property
    def event(self):
        return self._event

    #add to do's method
    def addToDo(self,toDo):
        """adds the toDo (string) action to the 
        collection. """
        return self._actions.append(toDo)

    #removeTodoItem method
    def removeToDoItem(self,index):
        #removes a to-do item using the 
        # index position of the todo item.
        if len(self._actions) > 0:
            self._actions.pop(index)
            return True
        else:
            return False

                
    def __str__(self):
        str_add = "Event: " + self.event + "\n"
        for i, action in enumerate(self._actions):
            str_add += str(i+1) + '. ' + str(action)+"\n"
        return str_add
        

def main():
    task = ToDo("Orientation camp")
    task.addToDo('Camp Fire')
    task.addToDo('BBQ')
    task.addToDo('Alcohol')
    print(task)
    task2 = ToDo('Study')
    task2.addToDo('Python')
    task2.addToDo('Computer Architecture')
    task2.addToDo('Data Analytics')
    print(task2)
main()

    