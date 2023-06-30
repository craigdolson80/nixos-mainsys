# flake.nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    hyprland.url = "github:hyprwm/Hyprland";
  };

  outputs = {nixpkgs, hyprland, ...}: {
    nixosConfigurations.nixosmain = nixpkgs.lib.nixosSystem {
      modules = [
        hyprland.nixosModules.default
        {programs.hyprland.enable = true;}
        # ...
      ];
    };
  };
}
