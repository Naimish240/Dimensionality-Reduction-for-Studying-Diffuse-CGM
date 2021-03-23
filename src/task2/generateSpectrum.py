# -----------------------------
# Created on 23rd March, 2021
# By Naimish Mani B
# -----------------------------
'''
This program contains all the modules required to generate
the spectrum of light passing through a slab of gas.

It has the following methods:

    calcAlpha
        Takes v and v0 (frequency) as inputs, and returns the absorption
        coefficient as output.

    calcIntensity
        Takes d (thickness), l (wavelength) and v0 (central frequency) as
        inputs, and returns the intensity of light for that wavelength as
        output.
'''
# -----------------------------
# Import Statements
from math import pi, exp
# -----------------------------
# Slab Properties
nH = 0.1  # cm -3
x = 0.1
# Hydrogen Properties (Lyman)
G = 6.265e8  # s -1
f = 0.4164
g0 = 2
Z = 2.0
# Other consts
me = 9.11e-28  # g
c = 3e10  # cm s -1
e = 4.80e-10  # cm 3/2 g 1/2 s-1
# -----------------------------


# Function to calculate the value of alpha
def calcAlpha(v, v0):
    '''
    Inputs :
        v : Frequency
        v0 : Central Frequency

    Output :
        a : Absorption Coefficient

    Formula taken from task 2 page 2
    '''
    A = (e * e * f * nH) / (4 * pi * me * c)
    B = ((1 - x) * g0) / (Z)
    C = (G) / ((v - v0) ** 2 + (G / (4 * pi)) ** 2)
    a = A * B * C
    return a


# Function to calculate Intensity
def calcIntensity(l, v0, d):
    '''
    Inputs :
        l : Wavelength
        v0 : Central Frequency
        d : Thickness of slab

    Output :
        I : (Intensity of light)

    Forumla taken from task 2 page 2
    '''
    # Calculates freq. from wavelength
    v = c / l
    # Calculates Alpha for wavelength and central freq.
    a = calcAlpha(v, v0)
    # Calculates Intensity for Alpha and d
    I = exp(a * d * -1)
    # Returns I
    return I


if __name__ == '__main__':
    print("Testing the functions to generate the spectrum!")
    print(calcIntensity(1015e-7, 2.4660))
