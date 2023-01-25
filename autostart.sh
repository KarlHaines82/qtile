#!/bin/bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# TODO: run_once
export QT_QPA_PLATFORMTHEME='qt5ct'

function run {
  if ! pgrep $1 > /dev/null ;
  then
    $@&
  fi
}
run picom
run blueman-applet
run nm-tray
~/.config/conky/restartconky.sh &
run dunst
dex -ae qtile -s ~/.config/autostart &
run xsettingsd

