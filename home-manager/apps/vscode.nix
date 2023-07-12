{config, pkgs, ...}:

{
 #VSCODE
     programs.vscode.enable = true;
     programs.vscode.enableExtensionUpdateCheck = true;
     programs.vscode.enableUpdateCheck = true;
     programs.vscode.extensions = [
	      pkgs.vscode-extensions.ms-python.python
        pkgs.vscode-extensions.jnoortheen.nix-ide
        pkgs.vscode-extensions.dracula-theme.theme-dracula
         ];
     programs.vscode.userSettings = {
        "editor.fontFamily" = "'Droid Sans Mono', 'monospace', monospace, 'FontAwesome'";
        "workbench.colorTheme" = "Dracula";
        "security.workspace.trust.untrustedFiles" = "open";
        "workbench.startupEditor" = "none";
        "git.openRepositoryInParentFolders" = "always";
          };
}
