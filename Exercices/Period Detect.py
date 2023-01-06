import os; os.system('cls')
import matplotlib.pyplot as plt
from math import pi, sin, nan

#-------------------------------------------------------------------------------
def GetPeriod(Tab):
  Period = 100            #replace with period compute
  Begin  = 10             #replace with begin  compute
  return Period, Begin    
#-------------------------------------------------------------------------------

#Create signal
x      = []
y      = []
offset = 25
phase  = 10

for i in range(200):
  j = phase + (i*2*pi/100)
  y.append( offset + (10 * sin(j)) + (5 * sin((j+4)*5)) )
  x.append(i)

#Analyze signal
period, begin = GetPeriod(y)   #get length and start of the signal period

#Plot full signal
fig = plt.figure("Full signal")
ax  = fig.subplots()
ax.plot(x,y)
ax.grid()
s = "Offset = {:d}     Phase = {:d}     Period = {:d}     Begin = {:d}".format(offset, phase, period, begin)
ax.text(0, 1.05, s, horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)

plt.show()

#Plot single period
xs = x    #replace with values for a single period
ys = y    #replace with subset of 'y' for a single period

fig = plt.figure("Single period signal")
ax  = fig.subplots()
ax.plot(xs,ys)
ax.grid()

plt.show()
