# Compound-V
### Disclaimer:
| This is a FORK of [Compound-V](https://github.com/survivalizeed/Compound-V), that implements a new [UI](https://prnt.sc/dy47vDOjuKUz), and a Random Aim/Bone selector.

| This **DOES NOT** change the core functionality of this project, which comes from [xx4-bfv-aimassist](https://github.com/exex4/xx4-bfv-aimassist)

| I am not a Python Developer. I have no idea what I'm doing. Don't complain about bugs.

- - - -

## Overview:
This project is a BFV aim-assist that implements the following features:
- A new UI that shows you your toggle status
  - Check out a screenshot [here](https://prnt.sc/dy47vDOjuKUz)
- Customizable Config/Keybinds
  - More Keycodes/Extra Keys
- Faster, Snappier Aiming/Targeting Switching
- Auto-Shoot 
  - Automatically shoot when holding Aim Key
- Auto-Scope
  - Automatically scope in when holding Aim Key
- Dodge-Mode
  - While holding Aim Key, spam crouch and uncrouch to make you harder to hit
- Hunt-Mode
  - Target a single player. Target distance is set to Unlimited, and you don't have to hold the Aim Key. Distance to target is also displayed.
- Keep-Target
  - Won't switch targets even if the target is behind an obstacle
- Bulletdrop Prediction
  - Measures the distance to the current target and offsets the pitch rotation by a well fitting factor

- - - -

## Installation:
1. Clone this repo, or download it from [here](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/notrespire/Compound-V)
2. Download and Install [Python](https://www.python.org/downloads/).
   1. Grab the latest version, and make sure it's added to your PATH.
3. Open your Terminal (Command Prompt/PowerShell/etc.), and navigate to this projects directory.
4. If you are using Python **v3.11.1** follow these steps:
   1. Install `pygame` using this command: `pip install pygame --pre`
   2. `pip install -r requirements.txt`
5. If you are on an older version of Python, run this command:
   1. `pip install -r requirements.txt`
6. Edit the Config in `main.py`
   1. Everything is documented, please read before asking questions.

- - - -

## How to use:
1. Load BFV first
2. Once the menu has loaded, open the included `.bat` file and let the program load
   1. If the `.bat` file instantly closes for you, you can use terminal to navigate to this projects folder, and run `python main.py`
3. Enter a Game.
4. Click your keybinds to verify that everything is loaded (You will hear a sound play)
5. Enjoy!

#### Use with recommendation
 - ##### [Tormund's Radar](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/70RMUND/Tormund-BFV-Radar)
  
#### RadarNameAddon
##### If you use Tormund's Radar and want to do a real hunt then replace the Radar.py with the Radar.py from the RadarNameAddon. This will add names to the Radar.
- - - -
