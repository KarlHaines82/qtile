#!/bin/sh
pulseaudio -D &
nitrogen --restore &
picom -b &
dunst &
dex -a -s $HOME/.config/autostart --environment qtile &
