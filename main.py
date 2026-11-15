import numpy as np
import matplotlib.pyplot as plt
import math
from odrpack import odr_fit

#0. setting up m convention
m = [0,1,2,-1,-2, 3, -3] #all the angles will be in this order
#use m[0:5] most of the time

#1. Read from file
def ReadFile(fileName: str):
    data = np.genfromtxt(fileName, delimiter=",", encoding="UTF-8-sig")
    data = np.transpose(data)
    data = [item[~np.isnan(item)] for item in data]
    return data

def AngleTransform(data: np.array):
    temp = [[], [], []]
    for i in range(3):
        degree = data[2*i+1]
        minute = data[2*i+2]
        degree_0 = degree[0]
        minute_0 = minute[0]
        angle = (degree_0 - degree) + (minute_0 - minute) / 60
        temp[i] = np.radians(angle)
    return temp
        
calibration = AngleTransform(ReadFile("Calibration.csv"))
darkblue = AngleTransform(ReadFile("DarkBlue.csv"))
lightblue = AngleTransform(ReadFile("LightBlue.csv"))
green = AngleTransform(ReadFile("Green.csv"))
red = AngleTransform(ReadFile("Red.csv"))
print(calibration)
print(darkblue)
print(lightblue)
print(green)
print(red)