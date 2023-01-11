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

def layout_ui(autoshoot, autoscope, autododge, keeptarget, fov, distance) -> layout:
    if autoshoot == True:
        styleShoot = "green"
    elif autoshoot == False:
        styleShoot = "red"
    
    if autoscope == True:
        styleScope = "green"
    elif autoscope == False:
        styleScope = "red"
        
    if autododge == True:
        styleDodge = "green"
    elif autododge == False:
        styleDodge = "red"
        
    if keeptarget == True:
        styleKeepTarget = "green"
    elif keeptarget == False:
        styleKeepTarget = "red"
    
    tableToggles = Table(title="Toggles:", show_lines=True, expand=True, box=box.ROUNDED, style="bright_black")
    tableToggles.add_column("Name", justify="left", style="bright_white", ratio=3),
    tableToggles.add_column("Status", justify="center", style="bright_white", ratio=1),
    tableToggles.add_row("AutoShoot", f"{autoshoot}", style=f"{styleShoot}"),
    tableToggles.add_row("AutoScope", f"{autoscope}", style=f"{styleScope}"),
    tableToggles.add_row("AutoDodge", f"{autododge}", style=f"{styleDodge}"),
    tableToggles.add_row("KeepTarget", f"{keeptarget}", style=f"{styleKeepTarget}"),
    tableToggles.add_row()
    tableToggles.add_row("FOV", f"{fov}", style="grey50")
    tableToggles.add_row("Distance", f"{distance}", end_section=True, style="grey50")

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

    layout["lower"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )

    layout["upper"].update(
        Align.center(
            Panel.fit(bannerText, title="v1.0", subtitle="Created by survivalizeed. UI by notRespire", style="light_slate_grey"),
        )
    )

    layout["right"].split_column(
        Panel(tableToggles),
    )

    layout["left"].update(
        Panel(
            Text("I have no idea how to get stdout to display here. help")
        )
    )
    return(layout)