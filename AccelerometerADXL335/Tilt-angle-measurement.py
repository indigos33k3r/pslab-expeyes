'''
GUI Program to plot acceleration data using ADXL335 sensor in real-time

ExpEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES
Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3


Accelerometer ADXL 335 can be used for measuring Tilt angle
ADXL335 acceleration measurement range is +/- 3 g. Supply voltage is 1.8 –  3.6 V, however all specifications at the datasheet is given at 3.0 V. This accelerometer has  3 outputs for X,Y,Z axis which voltage is proportional to acceleration on specific axis.

At midpoint when acceleration is 0 g output is typically 1/2 of supply voltage. If a supply voltage is 3V, then output is 1.5 V. Output sensitivity typically is 300 mV/g.

Calibration:
For calculating acceleration in terms of g
Ref: https://www.sparkfun.com/datasheets/Components/SMD/adxl335.pdf
For 	0g  	v = 1.61 volt
	-1g	v = 1.31 volt
	+1g 	v = 1.91 volt
Sensitivity 	0.3v/g

'''
import gettext					#Internationalization
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext


import time, math, sys
if sys.version_info.major==3:			# Python 3 compatibility
        from tkinter import *
else:
        from Tkinter import *

sys.path=[".."] + sys.path
from numpy import*
import expeyes.eyesj as eyes
import expeyes.eyeplot as eyeplot
import expeyes.eyemath as eyemath
p=eyes.open()

print p.set_voltage(3.6)   # set voltage at PVS  3.6v is operating voltage for ADXL335
		
t,v = p.get_voltage_time(1)  	# Read A1
v2 = p.get_voltage(2)		# Read A2
v3 = p.get_voltage(3)		# Read IN1

Xaccl = (v-1.6) / 0.3
Yaccl = (v2-1.6) / 0.3
Zaccl = (v3-1.6) / 0.3

angle_x =atan2(-Yaccl,-Zaccl)*57.2957795+180;	# math.atan2(y, x)-Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.


angle_y =atan2(-Zaccl,-Xaccl)*57.2957795+180;
angle_z =atan2(-Xaccl,-Yaccl)*57.2957795+180;

print angle_x
print angle_y
print angle_z
	
