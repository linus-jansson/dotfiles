#!/bin/sh
set -e
xset s off dpms 0 10 0
i3lock -n -i ~/Pictures/bgblur.png
xset s off -dpms
