"""This file is testing aspects of the os module that we want to store somewhere in our program including operating
system name and other attributes."""
import os
import platform
import distro

operating_system = os.uname()
print(operating_system)

"""This code does not locate the string, can be anywhere"""
if operating_system.__contains__("Linux"):
    print("It works")
else:
    print("Failed")

if operating_system[0] == "Linux":
    print("It works")
else:
    print("Failed")

"""
if operating_system['sysname'] == "Linux":
    print("It works")
else:
    print("Failed")
This section of code failed due to the fact that os.uname() returns a tuple and it cannot be called by the 
item identifying name such as sysname."""