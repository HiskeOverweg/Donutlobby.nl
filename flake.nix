{
  description = "groceries";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = "python3";
        ppkgs = pkgs."${python}Packages";
      in
      {
        devShell = pkgs.mkShell {
          nativeBuildInputs = [
            pkgs."${python}"
            ppkgs.black
            ppkgs.flake8
            ppkgs.pelican
            ppkgs.markdown
          ];
        };
      }
    );
}
