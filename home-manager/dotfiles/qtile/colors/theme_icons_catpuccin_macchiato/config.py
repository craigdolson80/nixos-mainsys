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
	return [["#282a36", "#282a36"], #color 0 Background
			["#44475a", "#44475a"], #color 1 Current Line
			["#44475a", "#44475a"], #color 2 Selection
			["#f8f8f2", "#f8f8f2"], #color 3 Foreground
			["#6272a4", "#6272a4"], #color 4 Comment
			["#8be9fd", "#8be9fd"], #color 5 Cyan
			["#50fa7b", "#50fa7b"], #color 6 Green
			["#ffb86c", "#ffb86c"], #color 7 Orange
			["#ff79c6", "#ff79c6"], #color 8 Pink
			["#bd93f9", "#bd93f9"],   #color 9 Purple
			["#ff5555", "#ff5555"], #color 10 Red
			["#f1fa8c", "#f1fa8c"], #color 11 Yellow
			["#FFFFFF", "#FFFFFF"], #color 12 White
			["#000000", "#000000"], #color 13 Black
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
       
   #Custom Key Combinations
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "g", lazy.spawn("geany"), desc="Launch Geany"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch PCManFM"),
    
   
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
            Match(wm_class=["irssi", "Microsoft Teams - Preview"]),
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
                     border_normal = colors[0],
                     border_width = 3,
                     margin = 10
                     ),
     layout.Columns(
                    border_focus = colors[9],
                    border_normal = colors[0],
                    border_width = 3,
                    margin = 10
                    ),
     layout.Max(),
    # Try more layouts by unleashing below layouts.
     layout.Stack(
                  border_focus = colors[9],
                  border_normal = colors[0],
                  border_width = 3,
                  margin = 10,
                  num_stacks=2
                  ),
	 layout.Bsp(
	            border_focus = colors[9],
                border_normal = colors[0],
                border_width = 3,
                margin = 10
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
    fontsize=14,
    padding=2,
    background=colors[0],
    foregroun=colors[12]
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
                            filename = "~/.config/qtile/colors/dracula/smaller_green_left.png",
                            scale = "False"
                           ),           
                widget.Image(
                             filename = "~/.config/qtile/icons/arch_linux_icon1.png",
                             mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(mymenu)},
                             scale = "False",
                             margin_x = 3,
                             background = colors[6],
                             margin_y = 3
                            ),
                widget.Image(
                            filename = "~/.config/qtile/colors/dracula/smaller_green_right.png",
                            scale = "False"
                           ),       
                widget.Sep(
                           linewidth = 0,
                           padding = 6
                           ),                            
                widget.GroupBox(
                                #highlight_color = colors[6],
                                #highlight_method = "line",
                                active = colors[6],
                                inactive = colors[12],
                                margin_y = 4,
                                margin_x = 0,
                                padding_y = 5,
                                padding_x = 2
                                ),
                               
                widget.Sep(
                           linewidth = 2,
                           padding = 18,
                           ),
                widget.WindowName(),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                             ),
              
				widget.CurrentLayout(
				           fontsize = 12,          
				             ),
				widget.CurrentLayoutIcon(),
				widget.Sep(
                           linewidth = 0,
                           padding = 6,
                           ), 
                widget.Systray(),
                widget.Image(
                            filename = "~/.config/qtile/colors/dracula/end_circle.png",
                            scale = "False"
                           ), 
                 widget.TextBox(
                               text = '',
                               background = colors[8],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 6
                               ),                                      
                widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "Updates: {updates} ",
                       foreground = colors[12],
                       colour_have_updates = colors[12],
                       colour_no_updates = colors[12],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                       padding = 5,
                       background = colors[8]
                       ),
                widget.Image(
                             filename = "~/.config/qtile/colors/dracula/leading_pink.png",
                             scale = "False"
                            ),
                widget.TextBox(
                              text = '',
                              background = colors[9],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 3
                               ),            
                widget.CPU(
                           background = colors[9],
						   foreground = colors[12],
						   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
						   padding = 6
                           ),
                widget.Image(
                             filename = "~/.config/qtile/colors/dracula/leading_purple.png",
                             scale = "False"
                            ),
                
                widget.TextBox(
                               text = '',
                               background = colors[8],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 3
                               ),
                widget.Memory(
                              measure_mem='G',
                              background = colors[8],
						      foreground = colors[12],
						      padding = 6
                              ),
                widget.Image(
                             filename = "~/.config/qtile/colors/dracula/leading_pink.png",
                             scale = "False"
                            ),                       
                widget.TextBox(
                               text = '',
                               background = colors[9],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 3
                               ),
                widget.Net(
						   #interface = "enp0s31f6",	
						   prefix = "M",
						   background = colors[9],
						   foreground = colors[12],
						   padding = 6
						   ),
                widget.Image(
                             filename = "~/.config/qtile/colors/dracula/leading_purple.png",
                             scale = "False"
                            ),      
                widget.TextBox(
                               text = '',
                               background = colors[8],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 3
                               ),
                widget.Clock(
                             format="%m-%d-%Y %H:%M",
                             background = colors[8],
						     foreground = colors[12],
						     padding = 6
                             ),
                widget.Image(
                             filename = "~/.config/qtile/colors/dracula/leading_pink.png",
                             scale = "False"
                            ),      
                 widget.TextBox(
                               text = '',
                               background = colors[9],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 3,
						       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('systemctl poweroff')}
                               ),
                widget.TextBox(
                               text = '',
                               background = colors[9],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 6,
						       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('systemctl restart')}
                               ),               
                widget.TextBox(
                               text = '',
                               background = colors[9],
						       foreground = colors[12],
						       fontsize = 14,
						       padding = 6,
						       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e killall qtile')},
                               ),
				#widget.Image(
                #             filename = "~/.config/qtile/colors/dracula/purple_left_end.png",
                #             scale = "False"
                #            ),		         
		       			  		         
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
