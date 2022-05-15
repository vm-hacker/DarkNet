#!/bin/bash

                #################### Anonstrike ####################
                #            Hack without being caught             #
                #            Developed & Maintained by:            #
                #   Netwrk-3, Inc: https://github.com/Netwrk-3     #
                #  Venkatesh Mishra: https://github.com/vm-hacker  #
                ####################################################
arg=$1

set -e
set -o pipefail  

if [ "$(id -u)" -ne 0 ];then
        printf "Anonstike needs root privilages!"
else
        if [ "$arg" = "--hostname" ];then
                # Hide Hostname
                old=$(cat /etc/hostname)
                new=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c12)
                sed -i "s/$old/$new/g" /etc/hosts
                sed -i "s/$old/$new/g" /etc/hostname
        elif [ "$arg" = "--mac" ];then
                # Hide MAC Adress
                ip link set wlan0 down
                macchanger -l > vendormac.txt
                ouimac=$(shuf -n 1 vendormac.txt | awk '{print$3}')
                uaamac=$(printf '%02x:%02x:%02x' $[RANDOM%256] $[RANDOM%256] $[RANDOM%256])
                macchanger -m "$ouimac:$uaamac" wlan0
                ip link set wlan0 up
        elif [ "$arg" = "on" ];then
                echo "Changing your ID!..."
                ip link set wlan0 down
                macchanger -l > vendormac.txt
                ouimac=$(shuf -n 1 vendormac.txt | awk '{print$3}')
                uaamac=$(printf '%02x:%02x:%02x' $[RANDOM%256] $[RANDOM%256] $[RANDOM%256])
                macchanger -m "$ouimac:$uaamac" wlan0
                ip link set wlan0 up
                old=$(cat /etc/hostname)
                new=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c12)
                sed -i "s/$old/$new/g" /etc/hosts
                sed -i "s/$old/$new/g" /etc/hostname
                echo "You're Anonymous now!"
        else
                printf "Error, Please use a valid Argument!"
        fi
fi

# Hide Timezone
#one=$(cat locl.txt | shuf -n 1)
#ln -sf /usr/share/zoneinfo/$one

exit 0
