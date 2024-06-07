#!/bin/bash
# remember that on your device the path will be different
LOGS_PATH=/home/pasha/Documents/Linux_club/UCU_Linux_Club/weeks/week8/solutions/my_logs.logs
CONF_PATH=~/.config/my_logs.conf
journalctl -b -x -p $(sed '2q;d' $CONF_PATH) > $LOGS_PATH
dmesg -d -l $(sed '3q;d' $CONF_PATH) >> $LOGS_PATH
