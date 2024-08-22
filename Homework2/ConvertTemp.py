#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:09:34 2024

@author: william
"""

import FtoC
import CtoF

def title():
    print('''Convert from C to F and Back
          By William Scott''')

def menu():
    print("A: Convert from Celsius to Fahrenheit")
    print("B: Convert from Fahrenheit to Celsius")
    convert = input("A or B or Exit: ")
    return convert


def main():
    
    convert = menu()

    if convert == "A" or convert == "a":
        print(str(round(CtoF.CtoF(float(input("Temp?: "))))) + "°F")
        
    elif convert == "B" or convert == "b":
        print(str(round(FtoC.FtoC(float(input("Temp?: "))))) + "°C")
    
    elif convert == "Exit" or convert == "exit":
        print("Goodbye!")
        return
    else:
        print("Please pick a valid option.")
    main()
    
    
title()
main()