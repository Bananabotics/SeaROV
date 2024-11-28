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
    left_joystick = controller.left_stick
    right_joystick = controller.right_stick

    '''
    ROV Layout:
    \_/  Theta = 32 degrees
    | |  The angled brackets represent the     
    /-\  Thrusters, Theta is with respect to
    the vertical axis.
    '''