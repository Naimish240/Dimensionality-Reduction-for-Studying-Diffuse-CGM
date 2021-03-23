# -----------------------------
# Created on 23rd March, 2021
# By Naimish Mani B
# -----------------------------
'''
This program contains the main glue required to get the stuff up and running
from the other scripts.
'''
# Imports
from spectrum import Spectrum

# v0 to store both central frequencies
# v0 has e18 because unit is m, not cm?
v0 = [2.46607e15, 2.46632e15]
# d to store all thicknesses
d = [10e14, 10e18, 10e21]

for i in v0:
    for j in d:
        obj = Spectrum(i, j, 10000, 1e-7, 1000e-7)
        obj.generate()
        print("-----------------------------")
        print("Number of wavelengths sampled: ", len(obj))
        print(obj)
        print("Wavelength of Minimum Intensity: ",
              obj.wavelengths[obj.intensities.index(min(obj.intensities))],
              "nm")
        print("Minimum Intensity: ",
              obj.intensities[obj.intensities.index(min(obj.intensities))])
        obj.show()
print("-----------------------------")