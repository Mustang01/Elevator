import Buttons
from enum import Enum
from Utilities import Event

class CallType(Enum):
    """Defines call types of panel; nice to have info"""
    UP=1
    DOWN=2

class CallPanelType(Enum):
    """Matters because different call panels have different buttons"""
    TOPFLOOR=1
    BOTTOMFLOOR=2
    ANYMIDDLEFLOOR=3
    
class CallPanel:
    """represents the type of panel with one or two buttons to summon the
    elevator"""
    up_button = None
    down_button = None
    
    def __init__(self, floor_changed_event, floor=0, 
                 call_panel_type=CallPanelType.ANYMIDDLEFLOOR):
        #only make an up button if not the top floor
        if(call_panel_type == CallPanelType.ANYMIDDLEFLOOR or 
           call_panel_type == CallPanelType.BOTTOMFLOOR):
            self.up_button = Buttons.ElevatorSystemButton(
                "up_button on floor "+str(floor),
                floor, floor_changed_event)
            self.up_button.pressed += self.button_press_up
        #only make a down button if not the bottom floor
        if(call_panel_type == CallPanelType.ANYMIDDLEFLOOR or 
           call_panel_type == CallPanelType.TOPFLOOR):
            self.down_button = Buttons.ElevatorSystemButton(
                "down_button on floor "+str(floor), floor, floor_changed_event)
            self.down_button.pressed += self.button_press_down
        #represents that this panel is generating a call, to the floor
        self.call = Event()
        self.floor = floor
        
    def _print_and_notify_call_info(self, elevator_system_button, call_type):
        print("Call panel on floor " + str(self.floor) + " has received a call from " + 
              elevator_system_button.name)
        self.call.notify(self, call_type)
        
    def button_press_down(self, elevator_system_button):
        """allows an external user to call the elevator to go down"""
        if(self.down_button != None):
            self._print_and_notify_call_info(elevator_system_button, CallType.DOWN)
        
    def button_press_up(self, elevator_system_button):
        """allows an external user to call the elevator to go up"""
        if(self.up_button != None):
            self._print_and_notify_call_info(elevator_system_button, CallType.UP)
    
            

class ElevatorPanel:
    """represents the type of panel that is inside the elevator car, with 
    buttons for the different floors"""
    
    def __init__(self, button_descriptors, floor_change_event):
        self._buttons = []
        for button_descriptor in button_descriptors:
            button = Buttons.ElevatorSystemButton(button_descriptor.name, 
                                                  button_descriptor.floor, 
                                                  floor_change_event)            
            button.pressed += self.button_press
            self._buttons.append(button)
            
        self.Request = Event()
        
    def button_press(self, elevator_car_panel_button):
        """button press by the user to go to a floor"""
        self.Request.notify(self, elevator_car_panel_button)
        

        
    
    
    