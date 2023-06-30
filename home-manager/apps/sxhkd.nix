{
 #SXHKD
 services.sxhkd = {
    enable = true;

 keybindings = {
  # Custom
    "super + Return" = "kitty";
    "super + b" = "firefox";
    "super + @space" = "$HOME/.config/rofi/launchers/type-3/launcher.sh";
    "super + Escape" = "pkill -USR1 -x sxhkd";

  #BSPWM
  # quit/restart bspwm
    "super + alt + {q,r}" = "bspc {quit,wm -r}";
  # Logout/Lock/Poweroff
    "super + ctrl + q" = "$HOME/.config/rofi/powermenu/type-2/powermenu.sh";
  # close and kill
    "super + {_,shift + }q" = "bspc node -{c,k}";
  # alternate between the tiled and monocle layout
    "super + m" = "bspc desktop -l next";
  # send the newest marked node to the newest preselected node
    "super + y" = "bspc node newest.marked.local -n newest.!automatic.local";
  # swap the current node and the biggest window
    "super + g" = "bspc node -s biggest.window";

#
# state/flags
#

  # set the window state
    "super + {t,shift + t,s,f}" = "bspc node -t {tiled,pseudo_tiled,floating,fullscreen}";
  # set the node flags
    "super + ctrl + {m,x,y,z}" = "bspc node -g {marked,locked,sticky,private}";

#
# focus/swap
#

  # focus the node in the given direction
    "super + {_,shift + }{h,j,k,l}" = "bspc node -{f,s} {west,south,north,east}";
  # focus the node for the given path jump
  # super + {p,b,comma,period}
  # bspc node -f @{parent,brother,first,second}
  # focus the next/previous window in the current desktop
    "super + {_,shift + }c" = "bspc node -f {next,prev}.local.!hidden.window";
  # focus the next/previous desktop in the current monitor
    "super + {Left,Right}" = "bspc desktop -f {prev,next}.local";
  # focus the last node/desktop
    "super + {grave,Tab}" = "bspc {node,desktop} -f last";
    # default config - replaced by "# KeyChord Focus / Send to desktiop on given monitor -- reddit post - IT WORKS"
  # focus or send to the given desktop
    "super + {_,shift + } {1,2} ; {1-9,0}" = "bspc {desktop -f, node -d} \"^{1,2}:^{1-9,10}\" --follow";
  # Change focused monitor
    "super + alt + {Left,Right}" = "bspc monitor -f {west,east}";
  # move and switch windows between monitors
    "super + {_,shift +} {comma, period}" = "bspc {monitor --focus,node --to-monitor} {prev,next} --follow";

#
# change window size
#

  # expand a window by moving one of its side outward
    "super + alt + {h,j,k,l}" = "bspc node -z {left -20 0,bottom 0 20,top 0 -20,right 20 0}";

  # contract a window by moving one of its side inward
    "super + alt + shift + {h,j,k,l}" = "bspc node -z {right -20 0,top 0 20,bottom 0 -20,left 20 0}";
		};
	 };
}
