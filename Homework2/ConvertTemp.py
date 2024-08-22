#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:09:34 2024

@author: william
"""

def FtoC(F): #Convert from Fahrenheit to Celsius"
    C = (F - 32) * 5 / 9
    return C

def CtoF(C): #Convert from Celsius to Fahrenheit
    F = (C * 9 / 5) + 32
    return F


def convertTemp():
    print("A: Convert from Celsius to Fahrenheit")
    print("B: Convert from Fahrenheit to Celsius")
    convert = input("A or B: ")

    if convert == "A" or convert == "a":
        print(CtoF(float(input("Temp?: "))))
        
    elif convert == "B" or convert == "b":
        print(FtoC(float(input("Temp?: "))))
    else:
        print("Please pick a valid option.")
        convertTemp()

convertTemp()