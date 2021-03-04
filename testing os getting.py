"""This file is testing aspects of the os module that we want to store somewhere in our program including operating
system name and other attributes."""
import os
import platform
import distro

operating_system = platform.system()
print(operating_system)
operating_system_version = platform.release()
python_version = platform.python_version()

"""This code does not locate the string, can be anywhere"""
if operating_system == "Windows":
    print("Windows")
    if operating_system_version in (8, 8.1, 10):
        print(operating_system_version)
    else:
        print("This os is not supported, we cannot guarantee that it will work, do you wish to proceed?")

elif operating_system == "Linux":
    print("Linux")
    print(operating_system_version)
else:
    print("This os is not supported, we cannot guarantee that it will work, do you wish to proceed?")
"""
This is how we could implement a check for Mac OS if we choose to support it in the future.
elif operating_system == "Darwin":
    print("Mac")
    print(operating_system_version)
"""


print (distro.linux_distribution())