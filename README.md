# ch340x_controller_v1.0
 This module is tested on windows 10 and windows 11.
 
 # Instructions
 Running with python:
 install requirements.txt
 
 Create instance of RelayController.Relay
```
hwid: str = '1A86:7523'
ch340T: Relay = Relay(device_hwid=hwid)
```

**Hardware ID or *hwid* for your device can be found using the pyserial library.**
```
```
