#!/bin/bash

#echo "Working..."

cat /var/log/fail2ban.log | grep -i notice | tail -n 1 > /home/pi/GPIO/log/last_log

if [[ $(cmp /home/pi/GPIO/log/last_log /home/pi/GPIO/log/tmp) ]]; then
        #echo "There is a new entry!"
        #cat /var/log/fail2ban.log | grep -i notice | tail -n 1
        cat /var/log/fail2ban.log | grep -i notice | tail -n 1 > /home/pi/GPIO/log/tmp
        cat /var/log/fail2ban.log | grep -i notice | tail -n 1 >> /home/pi/GPIO/log/history
        python /home/pi/GPIO/blink.py
#else
        #echo "Empty!"
fi
