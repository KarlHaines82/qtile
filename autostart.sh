#!/bin/sh
nitrogen --restore &
~/.config/conky/startconky.sh &
dunst &
dex -ae qtile &
