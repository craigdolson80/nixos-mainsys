{
  #ZSH
  programs.zsh = {
    enable = true;
    enableCompletion = true;
    enableAutosuggestions = true;
    syntaxHighlighting.enable = true;
    oh-my-zsh = {
      enable = true;
      plugins = [ "docker-compose" "docker" "ssh-agent" "git" ];
      theme = "michelebologna";
    };
    initExtra = ''
      bindkey '^f' autosuggest-accept
      neofetch
      alias vim="nvim"
      alias ls="exa -la --group-directories-first"
      alias cat="bat"
      alias rm="trash"
    '';
  };
}
