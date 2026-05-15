{
  description = "Flake for building this course contents";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-25.11";
  };

  outputs =
    { nixpkgs, ... }:
    let
      forAllSystems =
        function:
        nixpkgs.lib.genAttrs [
          "x86_64-linux"
          "aarch64-linux"
        ] (system: function nixpkgs.legacyPackages.${system});
    in
    {
      packages = forAllSystems (pkgs: {
        default = pkgs.stdenvNoCC.mkDerivation {
          pname = "digital-security";
          version = "1.0";

          src = ./latex;

          buildInputs = [
            pkgs.texliveFull
          ];

          buildPhase = ''
            runHook preBuild

            latexmk -pdf main.tex

            runHook postBuild
          '';

          installPhase = ''
            runHook preInstall

            mkdir $out
            cp main.pdf $out/main.pdf

            runHook postInstall
          '';
        };
      });

      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = [
            pkgs.texliveFull
          ];
        };
      });
    };
}
