{ config, pkgs, ... }:

let
  user="craig";
in
{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
      # Include modules
      modules/fonts.nix
      modules/vm.nix
      modules/polkit.nix
      modules/syspkgs.nix
      ];

  # Bootloader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  # Setup keyfile
  boot.initrd.secrets = {
    "/crypto_keyfile.bin" = null;
  };

  # Enable swap on luks
  boot.initrd.luks.devices."luks-93e656e6-7c35-4c9e-9de4-0192c77c1b2c".device = "/dev/disk/by-uuid/93e656e6-7c35-4c9e-9de4-0192c77c1b2c";
  boot.initrd.luks.devices."luks-93e656e6-7c35-4c9e-9de4-0192c77c1b2c".keyFile = "/crypto_keyfile.bin";

  networking.hostName = "nixosmain"; # Define your hostname.
  
  # Enable networking
  networking.networkmanager.enable = true;
  networking.hosts = {
  "10.0.1.2" = [ "synology" ];
  };
  
  fileSystems."/home/${user}/nfs" = {
    device = "synology:/volume1/${user}";
    fsType = "nfs";
    options = [ "x-systemd.automount" "noauto" ];
  };
      
  # Set your time zone.
  time.timeZone = "America/Chicago";

  # Select internationalisation properties.
  i18n.defaultLocale = "en_US.UTF-8";

  i18n.extraLocaleSettings = {
    LC_ADDRESS = "en_US.UTF-8";
    LC_IDENTIFICATION = "en_US.UTF-8";
    LC_MEASUREMENT = "en_US.UTF-8";
    LC_MONETARY = "en_US.UTF-8";
    LC_NAME = "en_US.UTF-8";
    LC_NUMERIC = "en_US.UTF-8";
    LC_PAPER = "en_US.UTF-8";
    LC_TELEPHONE = "en_US.UTF-8";
    LC_TIME = "en_US.UTF-8";
  };
  

  # Enable the X11 windowing system.
  services.xserver.enable = true;

  # Enable the Desktop Environment.
  services.xserver.displayManager.sddm.enable = true;
  services.xserver.desktopManager.plasma5.enable = true;
  services.xserver.windowManager.bspwm.enable = true;
  services.xserver.windowManager.qtile.enable = true;
  
  # MISC Services to enable
  services.pcscd.enable = true;
  programs.dconf.enable = true;
  services.trezord.enable = true;
  services.flatpak.enable = true;
  xdg.portal = {
     enable = true;
     extraPortals = [ pkgs.xdg-desktop-portal-gtk ];
  };

  # Configure keymap in X11
  services.xserver = {
    layout = "us";
    xkbVariant = "";
  };

  # Enable CUPS to print documents.
  services.printing.enable = true;
  services.avahi.enable = true;
  services.avahi.nssmdns = true;
  services.avahi.openFirewall = true;

  # Enable sound with pipewire.
  sound.enable = true;
  hardware.pulseaudio.enable = false;
  security.rtkit.enable = true;
  services.pipewire = {
    enable = true;
    alsa.enable = true;
    alsa.support32Bit = true;
    pulse.enable = true;
  };

  # Enable touchpad support (enabled default in most desktopManager).
  # services.xserver.libinput.enable = true;

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.craig = {
    isNormalUser = true;
    description = "${user}";
    extraGroups = [ "networkmanager" "wheel" "audio" "video" "lpd" "libvirtd" "users" ];
    packages = with pkgs; [
     #firefox
    ];
    shell = pkgs.zsh;
  };

 
  #Allow unfree packages
  nixpkgs.config.allowUnfree = true;
  
  programs.zsh.enable = true;
  
  # This value determines the NixOS release from which the default
  # settings for stateful data, like file locations and database versions
  # on your system were taken. It‘s perfectly fine and recommended to leave
  # this value at the release version of the first install of this system.
  # Before changing this value read the documentation for this option
  # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
  system.stateVersion = "23.05"; # Did you read the comment?
  
  nix.settings.experimental-features = [ "nix-command" "flakes" ];

### HOME MANAGER MODULE - MOVED TO FLAKE ###
  
}
