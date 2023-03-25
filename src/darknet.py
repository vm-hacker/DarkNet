#!/usr/bin/env python3

import colorama
from colorama import Fore
from art import *
import sys
import os
import time
import scannet

def help_menu():
    print(Fore.YELLOW + " [!] Help menu ")
    print(Fore.WHITE + """
  usage:
    scan (scan all machines in a network)
    vulnscan (scan all the machines in a network and list their vulnebilities)
    routeping (ping the Network's router)
    webscan (scan for a web server in the network)
    pktsniff (sniff the packets of the network)
    malpktinject (Inject malacious packets to the network)
    ipaddrlist (Show the IP addresses and the MAC addresses of the hosts on the network")
    dnmitm (Launch a Man in the Middle Attack)
  security:
    suspktscan (Scan for Suspicios packets)
    dtrhkr (Determine if a Attacker is in your Network)
    hkrvulnscan (Scan the Attacker's machine for vulnebilities)

 arguments:
    shell (Load the darknet shell)
""")

for i in range(1):
    print(" <<-------------- Copyright (c) Netwrk-3, Inc. All rights reserved ---------------->> ")
    #tprint("DarkNet") 
   # Art=text2art("Darknet",font='circle',chr_ignore=True)
    #print(Art) 
    tprint("Darknet")
    print("\033[1;32m DarkNet version 0.1.1")
    print(Fore.RED + " The most advanced Network Security tool ")
    print(Fore.BLUE + " Developed by Venkatesh Mishra ")

    print(Fore.YELLOW + " URL --> https://github.com/vm-hacker/darknet ")

def shell():
    cmd = input(Fore.YELLOW + "λ Darknet " + Fore.RED + ">" + Fore.GREEN + ">" + Fore.BLUE + "> " + Fore.WHITE)
    if cmd == "exit":
        for i in range(1):
            sys.exit()
    elif cmd == "scan":
        time.sleep(1) 
        #print(Fore.GREEN + "Scanning your network...")
        scannet.scan()
        print(Fore.GREEN + "Scan Completed!\n")
    elif cmd == "netwrkdn":
        print(Fore.GREEN + "Bringing down Network... ")
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-100s] %d%%" % ('#'*i, 1*i))
            time.sleep(0.25)
        
    elif cmd == "routeping":
        print(Fore.GREEN + "Determining router... \n")
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-100s] %d%%" % ('#'*i, 1*i))
            time.sleep(0.25)
        
        print("Resolving DNS... \n")
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-100s] %d%%" % ('#'*i, 1*i))
            time.sleep(0.25)

        print(Fore.YELLOW + " [!] Found target network's router. ")
    
    elif cmd == "?":
        for i in range(1):
            help_menu()
        
    # Execute shell commands from dn shell.
    else:
        for i in range(1):
            os.system(cmd)

if __name__ == "__main__":
    for i in range(1):
        n = len(sys.argv)
        for i in range(1, n):
            arg = sys.argv[i]
            if arg == "shell":
                print (Fore.YELLOW +  " [!] Darknet Shell Activated " )
                while True:
                    shell()
            elif arg == "hack":
                print(Fore.GREEN + " Hacking ain't done like this!  ")
            elif arg == "--help":
                for i in range(1):
                    help_menu()
            else:
                print(Fore.RED + " [!] Error: Please enter a valid argument ")

else:
    for i in range(1):
        pass
