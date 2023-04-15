# Sinple ch340x USB Relay Controller v1.0
 **This module is tested on:**
 Relay type: ch340T.
 OS-system: Windows 10, Windows 11.
 
 <img src="https://github.com/Isak-Landin/ch340x_controller_v1.0/blob/main/ch340T.jpg" width="350">
 
 # Instructions
 Running with python:
 install requirements.txt
 
 **Create instance of RelayController.Relay**
```
hwid: str = '1A86:7523'
ch340T: Relay = Relay(device_hwid=hwid)
```

**Hardware ID or *hwid* for your device can be found using the pyserial library.**
```
import serial
from serial.tools import list_ports_common
from serial.tools import list_ports

possible_relay_ports: list[serial.tools.list_ports_common.ListPortInfo] = serial.tools.list_ports.comports()

for port in possible_relay_ports:
    print(port.hwid)
```

> USB VID:PID=1A86:7523 SER= LOCATION=1-5

We take the hwid from the output, *1A86:7523*

Enjoy.
