{ config, pkgs, ... }:
let
  user="craig";
in
{
  environment.systemPackages = with pkgs; [
    bat
    trash-cli
    vim
    wget
    pavucontrol
    neofetch
    neovim
    killall
    exa
    vimPlugins.dracula-vim
    vimPlugins.dracula-nvim
    vimPlugins.catppuccin-vim
    vimPlugins.catppuccin-nvim
## Virtual Support Packages ##
    virt-manager
    virt-viewer
    spice spice-gtk
    spice-protocol
    win-virtio
    win-spice
##-------------------------##
    pciutils
    usbutils
    lm_sensors
    pcsclite
    pcsctools
    ccid
    trezor-udev-rules
    
#Ledger Live
 (writeShellScriptBin "ledger.sh" ''
   appimage-run "/home/${user}/Applications/Ledger.AppImage";
'')
#Trezor Suite
 (writeShellScriptBin "trezor.sh" ''
   appimage-run "/home/${user}/Applications/Trezor.AppImage";
'')

  ];
}
