#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:09:34 2024

@author: william
"""

import FtoC
import CtoF

def title():
    print('''Convert from °C to °F and Back
          By William Scott''')

def menu():
    print("A: Convert from Celsius to Fahrenheit")
    print("B: Convert from Fahrenheit to Celsius")
    convert = input("A or B or Exit: ")
    return convert


def getTemp():
    while True:
        try:
            temp = float(input("Temp?: "))
            break
        except ValueError:
            print("That's not a valid temperature, please try again.")
    return temp

def main():
    
    convert = menu()
    
    
    if convert == "A" or convert == "a":
        print(str(round(CtoF.CtoF(getTemp()))) + "°F")
        
    elif convert == "B" or convert == "b":
        print(str(round(FtoC.FtoC(getTemp()))) + "°C")
    
    elif convert == "Exit" or convert == "exit" or convert == "e":
        print("Goodbye!")
        return
    else:
        print("Please pick a valid option.")
        
    main()
    
    
title()
main()