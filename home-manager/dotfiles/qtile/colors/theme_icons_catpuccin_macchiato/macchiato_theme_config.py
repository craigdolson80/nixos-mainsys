import os
import re
import socket
import subprocess
from libqtile import bar, layout, widget, extension, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer

mod = "mod4"
mod1 = "control"
mod3 = "alt"
terminal = "alacritty"
mybrowser = "firefox"
myeditor = "geany"
mymenu = "rofi -show run"

##Autostart Script for misc applications##
@hook.subscribe.startup_once
def start_once():
	home = os.path.expanduser('~')
	subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

#CUSTOM COLORS - Catpuccin / Cappucino#
def init_colors():
	return [["#f4dbd6", "#f4dbd6"], #color 0 Rosewater
			["#f0c6c6", "#f0c6c6"], #color 1 Flamingo
			["#f5bde6", "#f5bde6"], #color 2 Pink
			["#c6a0f6", "#c6a0f6"], #color 3 Mauve
			["#ed8796", "#ed8796"], #color 4 Red
			["#ee99a0", "#ee99a0"], #color 5 Maroon
			["#f5a97f", "#f5a97f"], #color 6 Peach
			["#eed49f", "#eed49f"], #color 7 Yellow
			["#a6da95", "#a6da95"], #color 8 Green
			["#8bd5ca", "#8bd5ca"], #color 9 Teal
			["#91d7e3", "#91d7e3"], #color 10 Sky
			["#7dc4e4", "#7dc4e4"], #color 11 Sapphire
			["#8aadf4", "#8aadf4"], #color 12 Blue
			["#b7bdf8", "#b7bdf8"], #color 13 Lavender
			["#cad3f5", "#cad3f5"], #color 14 Text
			["#b8c0e0", "#b8c0e0"], #color 15 Subtext1
			["#a5adcb", "#a5adcb"], #color 16 Subtext0
			["#939ab7", "#939ab7"], #color 17 Overlay2
			["#8087a2", "#8087a2"], #color 18 Overlay1
			["#6e738d", "#6e738d"], #color 19 Overlay0
			["#5b6078", "#5b6078"], #color 20 Surface2
			["#494d64", "#494d64"], #color 21 Surface1
			["#363a4f", "#363a4f"], #color 22 Surface0
			["#24273a", "#24273a"], #color 23 Base
			["#1e2030", "#1e2030"], #color 24 Mantle
			["#181926", "#181926"], #color 25 Crust
			["#FFFFFF", "#FFFFFF"], #color 26 White
            ]

colors = init_colors()			

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "o", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawn(mymenu), desc="Run Rofi"),
       
   #Custom DMENU Launcher
   Key([mod, "control"], "Return", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="$",
        background="#24273a",
        dmenu_font="Ubuntu Bold-10",
      ))),
]

##This function auto changes to the group when an application is opened, if matched to a group##

@hook.subscribe.client_managed
def show_window(window):
     window.group.cmd_toscreen()

groups = [
    Group("1", label="term",
        matches=[
            Match(wm_class=["Alacritty"]),
        ]
          ),
               
    Group("2", label="www",
        matches=[
            Match(wm_class=["firefox","Google-chrome"]),
        ]
          ),

    Group("3", label="vm",
        matches=[
            Match(wm_class=["Virt-manager"]),
        ]
          ),

    Group("4", label="util",
        matches=[
            Match(wm_class=["Yubico Authenticator","Galculator"]),
        ]
          ),

    Group("5", label="dev",
        matches=[
            Match(wm_class=["Geany"]),
        ]
          ),

    Group("6", label="file",
        matches=[
            Match(wm_class=["pcmanfm", "Thunar"]),
        ]
          ),

    Group("7", label="chat",
        matches=[
            Match(wm_class=["irssi"]),
        ]
          ),

    Group("8", label="misc",
          ),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # mod4 + Shift + left or right arrow to move groups left or right
            Key(
                [mod], "Left", 
                 lazy.screen.prev_group()),
            Key(
				[mod], "Right",
				 lazy.screen.next_group()),
            
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
     layout.MonadTall(
                     border_focus = colors[9],
                     border_normal = colors[19],
                     border_width = 2,
                     margin = 6
                     ),
     layout.Columns(
                    border_focus = colors[9],
                    border_normal = colors[19],
                    border_width = 2,
                    margin = 6
                    ),
     layout.Max(),
    # Try more layouts by unleashing below layouts.
     layout.Stack(
                  border_focus = colors[9],
                  border_normal = colors[19],
                  border_width = 2,
                  margin = 6,
                  num_stacks=2
                  ),
	 layout.Bsp(
	            border_focus = colors[9],
                border_normal = colors[19],
                border_width = 2,
                margin = 6
	            ),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

## Widget defaults ##

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=13,
    padding=2,
    background=colors[23]
    )
extension_defaults = widget_defaults.copy()

##Mouse Callbacks##

screens = [
    Screen(
        top=bar.Bar(
            [            
                widget.Sep(
                           linewidth = 0,
                           padding = 6,
                           ),
                widget.Image(
                             filename = "~/.config/qtile/icons/green_python.png",
                             mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(mymenu)},
                             scale = "False"
                            ),
                widget.Sep(
                           linewidth = 0,
                           padding = 6,
                           ),                             
                widget.GroupBox(
                                highlight_color = colors[3],
                                highlight_method = "line",
                                margin_y = 4,
                                margin_x = 0,
                                padding_y = 5,
                                padding_x = 2
                                ),
                widget.Sep(
                           linewidth = 2,
                           padding = 12,
                           ),                 
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                             ),
              
				widget.CurrentLayout(),
				widget.CurrentLayoutIcon(),
				widget.Sep(
                           linewidth = 0,
                           padding = 6,
                           ), 
                widget.Systray(),                           
                widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "Updates: {updates} ",
                       foreground = colors[25],
                       colour_have_updates = colors[25],
                       colour_no_updates = colors[25],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                       padding = 5,
                       background = colors[0]
                       ),
                widget.Image(
                             filename = "~/.config/qtile/colors/theme_icons_catpuccin_macchiato/green_aarow.png",
                             scale = "False"
                            ),
                widget.CPU(
                           background = colors[8],
						   foreground = colors[25],
						   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e gtop')},
						   padding = 5
                           ),
                widget.Image(
                             filename = "~/.config/qtile/colors/theme_icons_catpuccin_macchiato/leading_green_aarow.png",
                             scale = "False"
                            ),
                widget.TextBox(
                               text = 'MEM:',
                               background = colors[3],
						       foreground = colors[25],
						       padding = 3
                               ),
               
                widget.Memory(
                              measure_mem='G',
                              background = colors[3],
						      foreground = colors[25],
						      padding = 5
                              ),
                widget.Image(
                             filename = "~/.config/qtile/colors/theme_icons_catpuccin_macchiato/leading_mauve_aarow.png",
                             scale = "False"
                            ),                       
                widget.Net(
						   interface = "enp0s31f6",	
						   prefix = "M",
						   background = colors[8],
						   foreground = colors[25],
						   padding = 5
						   ),
                widget.Image(
                             filename = "~/.config/qtile/colors/theme_icons_catpuccin_macchiato/leading_green_aarow.png",
                             scale = "False"
                            ),      
                widget.Clock(
                             format="%m-%d-%Y %H:%M",
                             background = colors[3],
						     foreground = colors[25],
						     padding = 5,
                             ),
                widget.Image(
                             filename = "~/.config/qtile/colors/theme_icons_catpuccin_macchiato/leading_mauve_aarow.png",
                             scale = "False"
                            ),      
                widget.QuickExit(
                                 background = colors[8],
						         foreground = colors[25],
						         padding = 5,
						         ),

				  		         
            ],
            
            24,
            
            opacity = 0.85       
            
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Yubico Authenticator'), # Yubioath Desktop
    Match(wm_class='Galculator')       # Galculator
])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True



# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
