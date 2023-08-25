# Python-Open-Hardware-Monitor
Python Window get CPU Temp by Open Hardware Monitor

## Ref:
https://stackoverflow.com/a/62936850

## Install
You could use OpenHardwareMoniter.dll. Use the dynamic library.

Firstly, Download the OpenHardwareMoniter. It contains a file called OpenHardwareMonitorLib.dll (version 0.9.6, December 2020).
https://openhardwaremonitor.org/downloads/


Install the module pythonnet:

pip install pythonnet


###Below code works fine on my PC (Get the CPU temperature):

```
import clr # the pythonnet module.
clr.AddReference(r'YourdllPath') 
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()
while True:
    for a in range(0, len(c.Hardware[0].Sensors)):
        # print(c.Hardware[0].Sensors[a].Identifier)
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print(c.Hardware[0].Sensors[a].get_Value())
            c.Hardware[0].Update()
```

### Attention
If you want to get the CPU temperature, you need to run it as Administrator. If not, you will only get the value of Load. For GPU temperature, it can work without Admin permissions (as on Windows 10 21H1).
