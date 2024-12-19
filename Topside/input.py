import inputs
import threading

#index is the controller value [First controller: 0, Second Controller: 1, etc.]
class controller:
    def __init__(self, index):
        self.right_stick = (0, 0)
        self.left_stick = (0, 0)
        self.right_trigger = 0
        self.left_trigger = 0
        self.a_pressed = 0
        self.x_pressed = 0
        self.b_pressed = 0
        self.y_pressed = 0
        self.select_pressed = 0
        self.start_pressed = 0
        self.left_bumper = 0
        self.right_bumper = 0
        self.device = inputs.devices.gamepads[index]
        self._thread()
        self.select_toggle = False
        self.start_toggle = False
    def _run(self):
        while True:
            for event in self.device.read():
                self._process_event(event)

    def _process_event(self, event):
        match str(event.code):
            case "ABS_X":
                self.left_stick = (event.state / 32768, self.left_stick[1])
            case "ABS_Y":
                self.left_stick = (self.left_stick[0], event.state / 32768)
            case "ABS_RX":
                self.right_stick = (event.state / 32768, self.right_stick[1])
            case "ABS_RY":
                self.right_stick = (self.right_stick[0], event.state / 32768)
            case "BTN_SELECT":
                self._process_select(event)
            case "BTN_START":
                self._process_start(event)
            case "BTN_EAST":
                self.b_pressed = ('1' if event.state == 1 else '0')
            case "BTN_WEST":
                self.x_pressed = ('1' if event.state == 1 else '0')
            case "BTN_NORTH":
                self.y_pressed = ('1' if event.state == 1 else '0')
            case "BTN_SOUTH":
                self.a_pressed = ('1' if event.state == 1 else '0')
            case "BTN_TL":
                self.left_bumper = ('1' if event.state == 1 else '0')
            case "BTN_TR":
                self.right_bumper = ('1' if event.state == 1 else '0')
            case "ABS_RZ":
                self.right_trigger = event.state
            case "ABS_Z":
                self.left_trigger = event.state
            case _:
                print(str(event.code) + ": " + str(event.state))

    def _process_select(self, event):
        if event.state == 1 and self.select_toggle == False:
            self.select_toggle = True
            self.select_pressed = '1'
        elif event.state == 1 and self.select_toggle == True:
            self.select_pressed = '0'
            self.select_toggle = False

    def _process_start(self, event):
        if event.state == 1 and self.start_toggle == False:
            self.start_toggle = True
            self.start_pressed = '1'
        elif event.state == 1 and self.start_toggle == True:
            self.start_pressed = '0'
            self.start_toggle = False
    
    def _thread(self):
        _run_thread = threading.Thread(target=self._run, daemon=True)
        _run_thread.start()