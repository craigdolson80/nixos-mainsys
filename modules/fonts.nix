{ config, pkgs, ... }:

{
  # Fonts
  fonts.fonts = with pkgs; [    
    font-awesome
    font-awesome_5
    font-awesome_4
    jetbrains-mono
    nerdfonts
    meslo-lgs-nf
    ubuntu_font_family
    google-fonts
  ];   
}
