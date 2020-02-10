import Panels
import Buttons
import time
import random
from Utilities import Event
from Elevator import ElevatorCar

class ElevatorSystem():
    """represents the full elevator system for a building.  Currently
    functions as the controller"""
    def __init__(self):
        # hardcode for now
        floors = 5
        # event for when the car moves to a different floor
        # one car for now, more to be added and this will change to a list
        self.car_1_floor_change = Event()
        
        #button descriptors, will be made to make all the elevator panel
        #buttons in the car. 
        button_descriptor_list = []
        for x in range(floors):
            button_name = "button"+str(x)
            button_descriptor_list.append(Buttons.ButtonDescriptor(button_name, x))
         
        #make CallPanels for each floor
        self.call_panels = []
        for x in range(floors):
            call_panel_type = Panels.CallPanelType.ANYMIDDLEFLOOR
            #get the call panel type right, per the floor
            if(x == 0):
                call_panel_type = Panels.CallPanelType.BOTTOMFLOOR
            elif(x==floors - 1):
                call_panel_type = Panels.CallPanelType.TOPFLOOR    
            call_panel = Panels.CallPanel(self.car_1_floor_change, x, 
                                         call_panel_type)
            call_panel.call += self.elevator_call_received
            self.call_panels.append(call_panel)             

        #make a new elevator panel, for the car
        self.elevator_panel = Panels.ElevatorPanel(button_descriptor_list, 
                                                  self.car_1_floor_change)
        #make the elevator car
        self.elevator_car = ElevatorCar("Car 1", self.elevator_panel)
        self.elevator_car.floor_changed += self.car_floor_change
        
        
    def _print_call_buttons(self, call_panel):
        if(call_panel.up_button != None):
            print("up_button floor " + str(call_panel.floor) + " is lit?: ", call_panel.up_button.lit())
        else:
            print("no up_button")
        if(call_panel.down_button != None):
            print("down_button floor " + str(call_panel.floor) + " is lit?: ", call_panel.down_button.lit())
        else:
            print("no down_button")
        
    def elevator_call_received(self, call_panel, call_type):
        """handler for when a call is received; instruct the elevator
        to go to the floor"""
        print("Call Received " + str(call_type))
        self._print_call_buttons(call_panel)
        self.elevator_car.go_to_floor(call_panel.floor)
    
    def car_floor_change(self, elevator):
        """handler for when the car moves.  Publish the event"""
        self.car_1_floor_change.notify(elevator.floor)
        self._print_call_buttons(self.call_panels[elevator.floor])
        
def main():
    """creates an elevator system for the building and plays with it"""
    elevator_system = ElevatorSystem()

    for i in range(10000):
        time.sleep(.5)
        if(i % 15 == 0):
            elevator_system.call_panels[random.randint(1,4)].down_button.press()
        if(i % 25 == 0):
            elevator_system.call_panels[random.randint(0,3)].up_button.press()


if __name__ == "__main__":
    main()


        
