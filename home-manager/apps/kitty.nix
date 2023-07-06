{
  #KITTY
  programs.kitty = {
  enable = true;
  font.name = "meslo-lgs-nf";
  font.size = 12;
  settings.scrollback_lines = "10000";
  };
	programs.kitty = {
	extraConfig = ''
	include /home/craig/nixos-mainsys/home-manager/dotfiles/kitty/kitty-themes/themes/Dracula.conf
	confirm_os_window_close 0
        background_opacity 0.8
        dynamic_background_opacity yes
    '';
  };

}
