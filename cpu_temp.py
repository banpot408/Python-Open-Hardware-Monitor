import clr # the pythonnet module.
import time
# clr.AddReference(r'D:\Dev\OpenHardwareMonitorLib') 
clr.AddReference(r'D:\PICO_ACS_BPP_DATA\05-Dev\Python-Open-Hardware-Monitor\OpenHardwareMonitorLib') 

# D:\PICO_ACS_BPP_DATA\05-Dev\Python-Open-Hardware-Monitor
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()
print(c)
print(c.Hardware)
while True:
    print("|-----------------------------------------------------------------------------------|")
    print("|----------          BPP ACS IoT READ CPU TEMPERATURE ON WINDOWN          ----------|")
    print("|-----------------------------------------------------------------------------------|")
    for a in range(0, len(c.Hardware[0].Sensors)):
        
        # print(c.Hardware[0].Sensors[a].Identifier)
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print(c.Hardware[0].Sensors[a].Identifier, " |---| ", c.Hardware[0].Sensors[a].get_Value())
            # print(c.Hardware[0].Sensors[a].get_Value())
            c.Hardware[0].Update()
    print("|-----------------------------------------------------------------------------------|")
    print("|----------                     PICO.CO.TH  & NXGE.CO                     ----------|")
    print("|-----------------------------------------------------------------------------------|")
    time.sleep(1)
    print()
    # exit()


