#!/usr/bin/python3

import sys
from my_pkg.bina import*
from my_pkg.union import*

while True:
    print("Select menu: 1) conversion 2) union/intersection 3) exit?")
    a = int(input())
    if a == 1:
        binary()
    if a == 2:
        listfunc()
    if a == 3:
        print("exit the program....")
        sys.exit()
