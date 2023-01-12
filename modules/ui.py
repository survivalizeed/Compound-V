from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
from rich.align import Align
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
from rich import box

console = Console()
layout = Layout()

def layout_ui(autoshoot, autoscope, autododge, keeptarget, fov, distance, huntMode, huntName, bone) -> layout:
    if autoshoot == True:
        autoshoot = "Enabled"
        styleShoot = "green"
    elif autoshoot == False:
        autoshoot = "Disabled"
        styleShoot = "red"
    
    if autoscope == True:
        autoscope = "Enabled"
        styleScope = "green"
    elif autoscope == False:
        autoscope = "Disabled"
        styleScope = "red"
        
    if autododge == True:
        autododge = "Enabled"
        styleDodge = "green"
    elif autododge == False:
        autododge = "Disabled"
        styleDodge = "red"
        
    if keeptarget == True:
        keeptarget = "Enabled"
        styleKeepTarget = "green"
    elif keeptarget == False:
        keeptarget = "Disabled"
        styleKeepTarget = "red"
        
    if huntMode == True:
        huntName = huntName
        styleHuntMode = "green"
    else:
        huntName = "Disabled"
        styleHuntMode = "red"
        
        
    table = Table(title="Options:", show_lines=True, expand=True, box=box.ROUNDED, style="bright_black")
    table.add_column("Name", justify="left", style="bright_white", ratio=3),
    table.add_column("Status", justify="center", style="bright_white", ratio=1),
    table.add_row("AutoShoot", f"{autoshoot}", style=f"{styleShoot}"),
    table.add_row("AutoScope", f"{autoscope}", style=f"{styleScope}"),
    table.add_row("AutoDodge", f"{autododge}", style=f"{styleDodge}"),
    table.add_row("KeepTarget", f"{keeptarget}", style=f"{styleKeepTarget}"),
    table.add_row("Hunt Mode", f"{huntName}", style=f"{styleHuntMode}"),

    table.add_row("FOV", f"{fov}", style="grey50")
    table.add_row("Distance", f"{distance}", style="grey50")
    table.add_row("Bone", f"{bone}", end_section=True, style="grey50")

    bannerText = """\
      _____                                  __   _   __
     / ___/__  __ _  ___  ___  __ _____  ___/ /__| | / /
    / /__/ _ \/  ' \/ _ \/ _ \/ // / _ \/ _  /___/ |/ / 
    \___/\___/_/_/_/ .__/\___/\_,_/_//_/\_,_/    |___/  
                /_/         
        """

    layout.split_column(
        Layout(name="upper", ratio=2),
        Layout(name="lower", ratio=5)
    )
    
    layout["upper"].update(
        Align.center(
            Panel.fit(bannerText, title="v1.0", subtitle="Created by survivalizeed. UI by notRespire", style="light_slate_grey", box=box.HORIZONTALS)
        )
    )

    layout["lower"].split_column(
        Panel(table, style="light_slate_grey", box=box.ROUNDED)
    )

    return(layout)
