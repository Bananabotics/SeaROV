from input import controller
from movement import pilot_logic
import constants

import socket
import time

try:
    pilot = controller(constants.pilot_index)
    operator = controller(constants.operator_index)
except IndexError as e:
    print(f"Error: No controller found. {e}")
    exit()

if constants.controller_testing == 0:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    packet = pilot_logic(pilot)
    print(packet)
    
    if constants.controller_testing == 0:
        sock.sendto(packet.encode(), (constants.UDP_IP, constants.UDP_PORT))
        
        # Receive response from the client
        try:
            sock.settimeout(1.0)  # Set timeout for receiving response
            response, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received response: {response.decode()}")
        except socket.timeout:
            print("No response received.")
    
    time.sleep(0.05)