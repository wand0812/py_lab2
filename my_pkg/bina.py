#!/usr/bin/python3

def binary():
binnum = input('input binary number : ')
two = '0b'
base = two + binnum
ten = int(base, 2)
eight = format(ten, 'o')
hexa = format(ten, 'X')
print("\n=> OCT> "+ eight)
print("=> DEC> ",ten)
print("=> HEX> "+ hexa) 
