from Utilities import Event

class ElevatorCar:
    """represents the actual elevator car"""
    def __init__(self, name, car_panel):
        self.name = name
        self.floor=0
        self.car_panel = car_panel
        self.floor_changed = Event()
        
        
    def go_to_floor(self, floor):
        """allows a controller to send this car to a floor.
        for now, just go there immediately"""
        print("Elevator " + self.name + " commanded to floor " + str(floor))
        #so easy to do in code
        self.floor = floor
        print("Elevator " + self.name + " arrived at floor " + str(floor))
        self.floor_changed.notify(self)
        
        
        