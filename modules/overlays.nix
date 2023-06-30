nixpkgs.overlays = [
  (self: super: {
    variety = super.variety.override {
      fehSupport = true;
    };
  })
];
