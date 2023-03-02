{ jacobi ? import
    (fetchTarball {
      name = "jacobi-2023-02-25";
      url = "https://nix.cobi.dev/x/4d4f5946e862bae2391493f471555c43cd753e99";
      sha256 = "00jwbhf1fn5xsmcybna6401mk011mn17zasz6qsngzzwdlcfb6kh";
    })
    { }
}:
let
  name = "automate_the_boring";


  tools = with jacobi; {
    cli = [
      coreutils
      nixpkgs-fmt
    ];
    python = [
      (python311.withPackages (p: with p; [
        pandas
        requests
      ]))
    ];
    scripts = [ ];
  };

  env = let paths = jacobi._toolset tools; in
    jacobi.buildEnv {
      inherit name;
      buildInputs = paths;
      paths = paths;
    };
in
env
