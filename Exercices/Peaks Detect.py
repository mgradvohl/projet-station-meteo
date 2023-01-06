import os; os.system('cls')
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------
def GetPeaks(Values, Min, Delta, Width):
    TabPos    : int   = []
    TabHeight : float = []

    TabPos.append(30);  TabHeight.append(Values[30])
    TabPos.append(60);  TabHeight.append(Values[60])

    return TabPos, TabHeight
#-------------------------------------------------------------------------------

#Define data
y = [
0, 0, 0.5, 0, 0.8, 0, 0, 0, 2, 6, 8, 7.5, 7, 5, 2, 1, 0, 0,
0, 3, 4, 3.5, 2, 0, 0, 0.5, 0,
0, 10.2, 15, 20.3, 20.1, 20, 12, 8, 6, 5, 5.5, 8, 10, 10.1, 10, 8.3, 4.2, 2, 1,
0, 0, 2, 4, 6, 2, 0, 0, 0.3, 0.5, 0, 0,
10, 14.5, 15, 14.8, 14.9, 12, 8, 14.8, 14.5, 6, 1, 2, 1, 0.5, 0.2, 0
]

x = range(len(y))

#Find peaks
peak_pos, peak_height = GetPeaks(Values = y, Min = 5, Delta = 2, Width = 10)

#Plot data + peaks
fig = plt.figure("Plotting peak detection")
ax  = fig.subplots()

ax.plot(x,y)
ax.scatter(peak_pos, peak_height, color = 'r', s = 50, marker = 'D', label = 'Peaks')
ax.legend()
ax.grid()

plt.show()
