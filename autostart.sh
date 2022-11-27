#!/bin/sh
#pulseaudio -D &
nitrogen --restore &
$HOME/.config/conky/startconky.sh &
picom -b &
dunst &
dex -a -s $HOME/.config/autostart --environment qtile &
