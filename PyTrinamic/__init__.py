'''
Created on 30.12.2018

@author: ED
'''

import serial.tools.list_ports;

from PyTrinamic import *
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_register
from PyTrinamic.ic.TMC5130.TMC5130_mask_shift import TMC5130_mask_shift

name = "PyTrinamic"
desc = "TRINAMIC's Python Technology Access Package"

def showInfo():
    print(name + " - " + desc)

def showAvailableComPorts():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)

    print("Available COM ports: " + str(connected))
    return 0;

def firstAvailableComPort():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
        return element.device;
