from constants import CY, SX, NEUTRAL, RANGE

def map_to_thrust(value):
    # value in [-1,1] -> 1000 to 2000
    return NEUTRAL + int(value * RANGE)

def pilot_logic(controller):
    '''
    ROV Layout (Rectangular, not square):
   t1   t2
    \__/     Theta = 32 degrees (with respect to the vertical axis)
    |..|     The angled brackets represent the     
    /--\     Thrusters, Theta is with respect to
   t3   t4   the vertical axis.
             The dots represent the up/down thrusters (tz1, tz2)
        Speeds:
            Neutral - 1500 ms
            Full Forward - 2000 ms
            Full Reverse - 1000 ms
    '''
    # Get joystick values
    lx, ly = controller.left_stick   # left stick X,Y in [-1,1]
    rx, _ = controller.right_stick  # right stick X,Y in [-1,1]

    # Get triggers and bumpers
    lt = controller.left_trigger / 255.0
    rt = controller.right_trigger / 255.0
    lb = 1 if controller.left_bumper == '1' else 0
    rb = 1 if controller.right_bumper == '1' else 0

    # Solve for horizontal thrusts (X, Y)
    # Avoid division by zero if angle is off:
    if abs(CY) < 1e-6 or abs(SX) < 1e-6:
        T1 = T2 = T3 = T4 = 0.0
    else:
        A = ly / (2 * CY)
        B = lx / (2 * SX)

        T1 = (A - B) / 2
        T2 = (A + B) / 2
        T3 = T1
        T4 = T2

    # Yaw from right stick X (rx):
    YAW_SCALE = 0.2
    T1 -= rx * YAW_SCALE
    T3 -= rx * YAW_SCALE
    T2 += rx * YAW_SCALE
    T4 += rx * YAW_SCALE

    # Roll from triggers:
    roll_input = rt - lt  # in [-1,1]
    ROLL_SCALE = 0.3
    tz1_roll = -roll_input * ROLL_SCALE
    tz2_roll =  roll_input * ROLL_SCALE

    # Vertical from bumpers:
    vertical_input = rb - lb
    VERT_SCALE = 1.0
    tz_base = vertical_input * VERT_SCALE

    # Combine vertical and roll:
    tz1 = tz_base + tz1_roll
    tz2 = tz_base + tz2_roll

    # Map to servo commands (1000-2000 µs)
    t1_cmd = map_to_thrust(T1)
    t2_cmd = map_to_thrust(T2)
    t3_cmd = map_to_thrust(T3)
    t4_cmd = map_to_thrust(T4)
    tz1_cmd = map_to_thrust(tz1)
    tz2_cmd = map_to_thrust(tz2)

    packet = ",".join(f"{cmd}" for cmd in [t1_cmd, t2_cmd, t3_cmd, t4_cmd, tz1_cmd, tz2_cmd])
    return packet