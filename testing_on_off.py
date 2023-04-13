from RelayController import Relay

"""
THIS IS A TEST SCRIPT!
Use this as an example of how to active your relay
"""

hwid: str = '1A86:7523'
ch340T: Relay = Relay(device_hwid=hwid)

last_power_state = None
while True:
    try:
        print('Please insert a 1 or a 0: ')
        on_or_off: str = input()

        if on_or_off == '1':
            if last_power_state != '1':
                if ch340T.turn_on():
                    last_power_state = '1'
            else:
                print('The device is already ON')
        elif on_or_off == '0':
            if last_power_state != '0':
                if ch340T.turn_off():
                    last_power_state = '0'
            else:
                print('The device is already OFF')
        else:
            print('Please provide me with a 1 or a 0')
            print('1 means ON, 0 means OFF')
    except KeyboardInterrupt:
        ch340T.turn_off()
        exit('Manual Shutdown')