
# https://askubuntu.com/questions/1110171/multi-monitor-setup-with-xrandr#1118470
xrandr \
  --output DP-2 --primary --mode 2560x1440 --pos 0x0 --rotate normal \
  --output HDMI-0 --mode 1920x1080 --right-of DP-2 --rotate left \
  --output HDMI-1 --mode 1920x1080 --left-of DP-2;
