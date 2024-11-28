from input import controller
import time
import requests



try:
    pilot_index = 0
    operator_index = 1
    pilot = controller(pilot_index)
    operator = controller(operator_index)
except IndexError as e:
    print("Error: Controllers Not Found")
    exit()

def pilot_logic(controller):
    '''
    ROV Layout (Rectangular, not square):
    \__/  Theta = 32 degrees
    |..|  The angled brackets represent the     
    /--\  Thrusters, Theta is with respect to
         the vertical axis.
         The dots represent the up/down thrusters
    '''
    left_joystick = controller.left_stick
    right_joystick = controller.right_stick

    left_bumper = controller.left_bumper
    right_bumper = controller.right_bumper