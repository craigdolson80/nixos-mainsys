services.picom with [
        enable = true;
        shadow = true;
        shadowOffsets [
            -3
            -3
        ]
        shadowOpacity = 0.60;
        shadowExclude = [
  "name = 'Notification'",
  "class_g = 'Conky'",
  "class_g ?= 'Notify-osd'",
  "class_g = 'Cairo-clock'",
  "class_g = 'slop'",
  "class_g = 'Polybar'",
  "class_g = 'trayer'",
  "_GTK_FRAME_EXTENTS@:c"
         ]
        fade = true;
        fadeSteps [
            0.03
            0.03
        ]
    fadeExclude = [
        "class_g = 'slop'"
        ]
         inactiveOpacity = 1.0;
         activeOpacity = 1.0;
         settings {
            frame-opacity = "1.00";
            inactive-opacity-override = "false";
            focus-exclude = "class_g = 'Bar";
            };     
         opacityRules = [
  "90:class_g    = 'Alacritty'",
  "100:class_g    = 'URxvt'",
  "100:class_g    = 'firefox'",
  "100:class_g    = 'Thunderbird'"    
            ]
         wintypes {
  normal = { fade = false shadow = true; };
  tooltip = { fade = true shadow = true; opacity = 0.75; focus = true; full-shadow = false; };
  dock = { shadow = opacity.services.picom.shadowExclude; };
  popup_menu = { opacity = config.services.picom.menuOpacity; };
  dropdown_menu = { opacity = config.services.picom.menuOpacity; };
         };
       ]