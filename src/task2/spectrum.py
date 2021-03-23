# -----------------------------
# Created on 23rd March, 2021
# By Naimish Mani B
# -----------------------------
'''
This program contains a class to generate
the spectrum of light passing through a slab of gas.

It has the following class:

    Spectrum
        Variables:
            v0 : central frequency for the spectrum
            d : thickness of slab for spectrum
            intensities : list of intensity for each wavelength

        Methods:
            __init__
                Creates object of class
                Requires 'v0' and 'd'

            generate
                Generates the spectrum for the object
                Requires 'res', 'l', 'u'

            show
                Shows the spectrum generated for the object
                Saves plot if flag is true

            __len__
                Returns the number of elements in Intensities

            __repr__
                Prints the values of v0 and d for the object
'''
# Import Statements
from generateSpectrum import calcIntensity
import os
import matplotlib.pyplot as plt


class Spectrum(object):
    def __init__(self, v0, d, res, low, up):
        '''
        Inputs :
            v0 : Central Frequency
            d : Thickness of slab
            res : Number of steps between low and up
            low : Lower limit / frequency to start from
            up : Upper limit / frequency to terminate generation at
        '''
        self.v0 = v0
        self.d = d
        self.res = res
        self.low = low
        self.up = up
        self.wavelengths = []
        self.intensities = []

    def generate(self):
        '''
        Generates list of intensities for the spectrum
        '''
        # Clears list of intensities and wavelengths
        self.intensities = []
        self.wavelengths = []
        # Finds the step value for the simulation
        STEP = (self.up - self.low) / self.res
        # Runs for loop, iterating across all wavelengths
        for i in range(self.res):
            # Wavelength
            w = self.low + (i * STEP)
            # Add wavelength to list of wavelengths
            self.wavelengths.append(w * 10**7)
            # Calculate intensity for wavelength
            intensity = calcIntensity(w, self.v0, self.d)
            # Add intensity to list of intensities
            self.intensities.append(intensity)

    def show(self, save=False):
        plt.plot(self.wavelengths, self.intensities)
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Intensity")
        plt.title("Spectrum")
        plt.show()
        if not save:
            return None

        if not os.path.exists('Plots'):
            os.mkdir('Plots')

        plt.savefig(f'Plots/{self.v0}_{self.d}_{self.res}_{self.low}_{self.up}.jpg')

    def __len__(self):
        return len(self.intensities)

    def __repr__(self):
        return f"Central Frequency : {self.v0}\nThickness of slab : {self.d}"


if __name__ == '__main__':
    print("Error! Can only import this script!")
