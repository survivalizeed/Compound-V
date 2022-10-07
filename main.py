from tkinter import N
from lib import aimer
from lib import helpers
from lib import keycodes
from lib.bones import bones
import time
import ctypes

#### CHANGE OPTIONS HERE ####

# Field of View
# Alter this between 0.1 and 3.0 for best results. 0.1 is very narrow, while larger numbers allow
# for more soldiers to be targeted
fov = 2.0

# Distance Limit
# Example, set to 75 to limit locking onto soldiers further than 100 meters away.
distance_limit = 75 # can also be: None

# Trigger Button
# Grab your preferred button from lib/keycodes.py
trigger = keycodes.XBUTTON2

# If set to True your weapon will automatically shoot after finding a target
autoshoot = True

# If set to True your weapon will automatically scope as soon as you lock onto a target
autoscope = True

huntToggle = keycodes.NUMPAD5

huntTargetSwitch = keycodes.NUMPAD8

# Aim Location Options
# Aim Location Switching (default is the first one listed)
# Check available bones in lib/bones.py
aim_locations = [bones['Head'], bones['Spine'], bones['Neck'], bones['Hips']]

# Key to switch aim location (set to None to disable)
aim_switch = keycodes.END
#aim_switch = None

# Normally, you won't need to change this
# This will attempt to gather your primary screen size. If you have issues or use
# a windowed version of BFV, you'll need to set this yourself, which probably comes with its own issues
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
# or
#screensize = (1280, 960)

collection = [fov, distance_limit, trigger, autoshoot, autoscope, aim_locations, aim_switch, screensize, huntToggle, huntTargetSwitch]

#### END OF CHANGE OPTIONS ####



if __name__ == "__main__":
    if fov < 0.1 or fov > 3.0:  # you can delete this if you know what you're doing
        print("Check your fov settings.")
        exit(1)
    if distance_limit is not None and distance_limit <= 0:
        print("Check your distance_limit settings")
        exit(1)

    print("BFV-AimBot ---> xx4 aim assist Version 0.5 as core and further developed by survivalizeed")
    print("Change or tweak options in the main.py file")
    print("Change the aim target with the END key")
    print("Head -> Spine -> Neck -> Hips")
    print()
    if not helpers.is_admin():
        print("- Error: This must be run with admin privileges")
        input("Press Enter to continue...")
        exit(1)

    if not helpers.is_python3():
        print("- Error: This script requires Python 3")
        raw_input("Press Enter to continue...")
        exit(1)

    arch = helpers.get_python_arch()
    if arch != 64:
        print("- Error: This version of Python is not 64-bit")
        input("Press Enter to continue...")
        exit(1)

    print ("Using screensize: %s x %s" % screensize)
    aimer = aimer.Aimer(collection)
    aimer.start()