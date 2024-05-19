#!/bin/sh

setxkbmap gb &
xset s off -dpms &
nm-applet --indicator &
pa-applet &
picom &
lxsession &