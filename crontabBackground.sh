#!/bin/bash
# export DISPLAY=:0
# gsettings set org.gnome.desktop.background picture-uri $(ls /home/endika/Background500px/*.jpg | shuf -n 1)

PID=$(pgrep gnome-session | tail -n1)
echo $PID
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

DIR="/home/endika/Background500px/"
PIC=$(ls $DIR/*.jpg | shuf -n1)
gsettings set org.gnome.desktop.background picture-uri "file://$PIC"

for VARIABLE in 1 2 3 4 5 6 7 8 9 10 11 12
do
    PIC=$(ls $DIR/*.jpg | shuf -n1)
    gsettings set org.gnome.desktop.background picture-uri "file://$PIC"
    sleep 5
done