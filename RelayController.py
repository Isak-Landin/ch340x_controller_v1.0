import codecs

import serial
import serial.tools.list_ports
import serial.tools.list_ports_common

"""
Relay Object
"""


class Relay:
    def __init__(self, device_hwid: str,
                 on_code: bytes = codecs.decode(b'A00101A2', 'hex'),
                 off_code: bytes = codecs.decode(b'A00100A1', 'hex')):
        """

        :param device_hwid: str: The hardware id, also known as hwid, for the relay you are setting up:
        :param on_code: bytes: hexadecimals in byte format: optional:
        :param off_code:  bytes: hexadecimals in byte format: optional:
        """
        self.port_name = None
        self.device_hwid = device_hwid
        self.on_hex = on_code
        self.off_hex = off_code
        if self.perform_port_availability_check():
            self.relayPort = serial.Serial(self.port_name, 9600, timeout=1)
            print('Device is ready!')
        else:
            self.relayPort = None
            print('No device was found during the checkup process')

    def perform_port_availability_check(self):
        possible_relay_ports: list[serial.tools.list_ports_common.ListPortInfo] = serial.tools.list_ports.comports()
        device_found: bool = False

        for port in possible_relay_ports:
            if self.device_hwid in port.hwid:
                self.port_name = port.name
                device_found = True
                break

        return device_found

    def turn_on(self):
        performed: bool = False
        if self.relayPort:
            try:
                self.relayPort.write(codecs.decode(b'A00101A2', 'hex'))
                performed = True
            except Exception:
                print('Device was set up but error occurred')
                print(Exception)
        else:
            print('No device')

        return performed

    def turn_off(self):
        performed: bool = False
        if self.relayPort:
            try:
                self.relayPort.write(codecs.decode(b'A00100A1', 'hex'))
                performed = True
            except Exception:
                print('Device was set up but error occurred')
                print(Exception)
        else:
            print('No device')

        return performed


"""# possible_relay_ports: list[serial.tools.list_ports_common.ListPortInfo] = serial.tools.list_ports.comports()
# A00101A2 ON
# A00100A1 OFF

# command that executes
# print(ser.write(codecs.decode(b'A00100A1', 'hex')))

# print(type(codecs.decode(b'A00100A1', 'hex')))"""


