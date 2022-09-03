# URAP PRROJECT

#references :

import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import pi
from mpl_toolkits.mplot3d import Axes3D

#water properties


#caluclate terminal velcoity
rho = 997
m = 1
g = 9.81
dia = 0.01
h = 1
vel = 1
def TerminalVel(h):
    vel1 = math.sqrt(2 * 9.81 * h)
    return vel1
TerminalVel(h)

#calculate the drag coefficient

def dragCoeff(m,g,rho,vel,dia):

    cf = (8* m* g) / (rho * vel**2 * dia * pi )
    return cf
dragCoeff(m,g,rho,vel,dia) # example values

def calculateDrag(rho, vel,cf,area):
    force_drag = rho * vel**2 * cf * area / 2
    return force_drag
calculateDrag(997,14,1,1)

# plot the as a function of
# plot of draf force vs velocity

a = 0.45
rho1 = 997
rho2 = 500
rho3 = 200
rho4 = 1500
# fluida
dfa1 = []
dfa2 = []
#fluidb
dfb1 = []
dfb2 = []
#fluidc
dfc1 = []
dfc2 = []
#fluidd
dfd1 = []
dfd2 = []

#random velocity values
velocity = [1,3,6,9,12,15]

coff1 = []
coff2 = []
coff3 = []
coff4 = []
arr1 = []
arr2 = []
arr3 = []
arr4 = []

# calculate the drag coefficients
for v in velocity :
    coff1.append((8 * m * g)/(rho1 * v * v * dia * pi))
arr1.append(coff1)

for v in velocity :
    coff2.append((8 * m * g)/(rho2 * v * v * dia * pi))
arr2.append(coff2)

for v in velocity :
    coff3.append((8 * m * g)/(rho3 * v * v * dia * pi))
arr3.append(coff3)

for v in velocity :
    coff4.append((8 * m * g) / (rho4 * v * v * dia * pi))
arr4.append(coff4)
a1 = np.round(arr1,3)
a2 = np.round(arr2,3)
a3 = np.round(arr3,3)
a4 = np.round(arr4,3)

print('coeff of fluid 1 =',a1)
print('coeff of fluid 2=',a2)
print('coeff of fluid 3 =', a3)
print('coeff of fluid 4 =', a4)


# get the drag force and put them in arrays

#fluida
for d in coff1:
    for v in velocity:
        dfa1.append(0.5 * a * rho1 * v * v * d)
    dfa2.append(dfa1)
    dfa1 = []
dfa3 = np.transpose(dfa2)

#fluidb
for d in coff2:
    for v in velocity:
        dfb1.append(0.5 * a * rho2 * v * v * d)
    dfb2.append(dfb1)
    dfb1 = []
dfb3 = np.transpose(dfb2)

#fluidc
for d in coff3:
    for v in velocity:
        dfc1.append(0.5 * a * rho3 * v * v * d)
    dfc2.append(dfc1)
    dfc1 = []
dfc3 = np.transpose(dfc2)

#fluidd
for d in coff4:
    for v in velocity:
        dfd1.append(0.5 * a * rho4 * v * v * d)
    dfd2.append(dfd1)
    dfd1 = []
dfd3 = np.transpose(dfd2)

da1 = np.round(dfa3,3)
da2 = np.round(dfb3,3)
da3 = np.around(dfc3,3)
da4 = np.around(dfd3,3)

print('drag force of flduid 1 =',da1)
print('drag force of fluid 2=', da2)
print('drag force of fluid 3 =', da3)
print('drag force of fluid 4 =', da4)

plt.figure(1)
plt.plot(velocity,da1)
plt.ylabel('Drag Force [N]')
plt.xlabel('Velocity')
plt.title('Drag vs Velocity of Fluid A ')

plt.figure(2)
plt.plot(coff1,da1)
plt.xlabel('Drag Coefficient')
plt.ylabel('Drag Force [N]')
plt.title('Drag Force vs Drag Coefficients of Fluid A')
plt.show()

plt.figure(3)
plt.plot(velocity,da2)
plt.ylabel('Drag Force [N]')
plt.xlabel('Velocity')
plt.title('Drag vs Velocity of Fluid B')

plt.figure(4)
plt.plot(coff2,da2)
plt.xlabel('Drag Coefficient')
plt.ylabel('Drag Force [N]')
plt.title('Drag Force vs Drag Coefficients of Fluid B')
plt.show()

plt.figure(5)
plt.plot(velocity,da3)
plt.ylabel('Drag Force [N]')
plt.xlabel('Velocity [m/s]')
plt.title('Drag vs Velocity of Fluid C')

plt.figure(6)
plt.plot(coff3,da3)
plt.xlabel('Drag Coefficient')
plt.ylabel('Drag Force [N]')
plt.title('Drag Force vs Drag Coefficients of Fluid C')
plt.show()

plt.figure(7)
plt.plot(velocity,da3)
plt.ylabel('Drag Force [N]')
plt.xlabel('Velocity [m/s]')
plt.title('Drag vs Velocity of Fluid C')

plt.figure(8)
plt.plot(coff3,da3)
plt.xlabel('Drag Coefficient')
plt.ylabel('Drag Force [N]')
plt.title('Drag Force vs Drag Coefficients of Fluid C')
plt.show()

plt.figure(9)
plt.plot(velocity,da4)
plt.ylabel('Drag Force [N]')
plt.xlabel('Velocity [m/s]')
plt.title('Drag vs Velocity of Fluid D')

plt.figure(10)
plt.plot(coff4,da4)
plt.xlabel('Drag Coefficient')
plt.ylabel('Drag Force [N]')
plt.title('Drag Force vs Drag Coefficients of Fluid D')
plt.show()


#mesh plot

