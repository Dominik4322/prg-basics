###
# program that calculates the distance to the horizon from a height given in meters from the keyboard
#    d is the distance to the horizon in kilometers
#   h is the height of the observer in meters
import math
d = float(input("Enter the height of the observer in meters: "))
h = math.sqrt(d * 3.57) * 1000
print(h)