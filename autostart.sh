#!/bin/sh
pulseaudio -D &
nitrogen --restore &
picom -Cb &
dunst &
xsettingsd &
dex -a -s $HOME/.config/autostart --environment qtile &
kdeconnect-indicator &
