{
  description = "ITPD autochecker development shell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/79b35bf0bda5cd110f856aa5b5b2c5ba4460dbf5";
    systems.url = "github:nix-systems/default/future-26.11";
    flake-parts = {
      url = "github:hercules-ci/flake-parts/17c9d6cdfc60c64f4ee8d306f9bc0b4ccb51481e";
      inputs.nixpkgs-lib.url = "github:nix-community/nixpkgs.lib";
    };
    backlog-md.url = "github:time-tools/Backlog.md/fd20f71493fb4eda44b021aa89f257956f17fb71";
  };

  outputs = inputs@{ flake-parts, systems, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import systems;

      perSystem = { pkgs, system, ... }:
        let
          python = pkgs.python313;
        in
        {
          devShells.default = pkgs.mkShell {
            packages = [
              python
              pkgs.uv
              pkgs.markdownlint-cli2
              pkgs.gh
              # pdftotext for reading the Moodle submission PDFs
              pkgs.poppler-utils
              pkgs.unzip
              pkgs.jq
              pkgs.ripgrep
              pkgs.lychee
              inputs.backlog-md.packages.${system}.default
            ];
            shellHook = ''
              export BACKLOG_CWD="$PWD"
              # Make uv use the pinned interpreter instead of downloading one.
              export UV_PYTHON="${python}/bin/python3"
              export UV_PYTHON_DOWNLOADS=never
            '';
          };
        };
    };
}
