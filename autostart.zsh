#!/bin/sh
#pulseaudio -D &
#xrandr --output Virtual-1 --mode 1920x1080 &&
nitrogen --restore &
picom -b &
dunst &
dex -a -s $HOME/.config/autostart --environment qtile &
