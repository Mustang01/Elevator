from Utilities import Event

class ButtonDescriptor:
    """can be used to describe buttons to create them"""
    def __init__(self, name, floor):
        self.name = name
        self.floor=floor
    
class ElevatorSystemButton(ButtonDescriptor):
    """represents any button in an elevator system; 
    activation, cleared on an external signal (
    elevator reaches a floor), has a light"""
    def __init__(self, name, floor, clearing_event):
        ButtonDescriptor.__init__(self, name, floor)
        self.pressed=Event()
        self.cleared=Event()
        self.__lit=False
        clearing_event += self.clear
    
    def press(self):
        """allows an external user to press the button"""
        self.__lit=True
        self.pressed.notify(self)
    
    def clear(self, floor):  
        """handler for the clear event; presumably the 
        elevator has arrived, can clear the light"""
        if(self.floor == floor):
            self.__lit=False
            self.cleared.notify(self)
        
    def lit(self):
        """accesses the private light variable"""
        return self.__lit
    
    
        
        
       
        
        
