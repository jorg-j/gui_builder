{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell rec {
  buildInputs = [
    pkgs.poetry
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.python3Packages.virtualenv
    pkgs.python3Packages.setuptools
    pkgs.python3Packages.black
    pkgs.python3Packages.pytest
    pkgs.python3Packages.isort
    pkgs.python3Packages.pip-tools
    pkgs.python3Packages.pyautogui
    # pkgs.python3Packages.curses
    pkgs.cmake
  ];

  # Prevent numpy from shitting itself
  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";

  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib"
    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath buildInputs}:$LD_LIBRARY_PATH"
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib.outPath}/lib:$LD_LIBRARY_PATH"
    python3 -m doctest main.py && python3 main.py
    exit
  
  '';
}

