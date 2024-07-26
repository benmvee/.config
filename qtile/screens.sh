#!/bin/bash
while true; do

    if xrandr | grep "HDMI-1 connected"; then
        xrandr --output HDMI-1 --auto --primary
    else
        xrandr --output eDP-1 --auto --primary
        xrandr --output eDP-1 --scale 0.5x0.5
    fi

    sleep 5
done
