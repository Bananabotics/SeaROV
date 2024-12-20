from math import radians, cos, sin

# Testing
#**********************************#
controller_testing = 0
#**********************************#

# Controller Constants
#**********************************#
pilot_index = 0
operator_index = 1
#**********************************#

# Speed Constants (In percentage, ex: 0.5 = 50%)
#**********************************#'''
ROV_Speed = 1.0
#**********************************#

#Network Constants
#**********************************#
UDP_IP = "192.168.1.177" # Replace with the IP address of the receiver
UDP_PORT = 8888          # Replace with the port number of the receiver
#**********************************#

# Movement Constants
#**********************************#
ANGLE_DEG = 32
ANGLE_RAD = radians(ANGLE_DEG)
CY = cos(ANGLE_RAD)
SX = sin(ANGLE_RAD)

NEUTRAL = 1500
RANGE = 500 * ROV_Speed
#**********************************#

'''
Deep Diver
By: ChatGPT

Beneath the waves, where sunlight fades,
The ROV glides through oceanic shades.
Its lights pierce the watery gloom,
Exploring depths where mysteries bloom.

Propellers hum, a gentle tune,
Mapping secrets under the moon.
With robotic grace, it probes and finds,
The hidden wonders of currents and tides.

A sentinel of science, bold and free,
Unveiling the treasures beneath the sea.
Through coral reefs and sunken lore,
The ROV dreams of depths to explore.
'''