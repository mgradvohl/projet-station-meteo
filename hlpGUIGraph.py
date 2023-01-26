#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpGUIGraph - Helper for plotting Graph & Chart on GUI                              JYC-2022
#-----------------------------------------------------------------------------------------------------------------------

from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------------------------------------------------
class GraphPlot:
    def __init__(self, root, canvas):
        fig = Figure(dpi=100)
        fig.set_tight_layout({"pad" : 1})
        self.subplot = fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().place(in_=canvas, relwidth=1, relheight=1)

    def Plot(self, ax, ay):
        self.subplot.clear()
        self.subplot.plot(ax, ay)
        self.subplot.set(xlabel="Temps (ms)", ylabel="Volts", autoscaley_on=False, ylim=(-0.1, 5.2))
        self.canvas.draw()

#-----------------------------------------------------------------------------------------------------------------------
class ChartPlot:
    def __init__(self, root, canvas, nbpoints):
        self.nbpoints : int   = nbpoints
        self.historic : float = []

        fig = Figure(dpi=100)
        fig.set_tight_layout({"pad" : 1})
        self.subplot = fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().place(in_=canvas, relwidth=1, relheight=1)

    def Plot(self, value):
        if len(self.historic) >= self.nbpoints:
            self.historic.pop(0)
        self.historic.append(value)

        self.subplot.clear()
        self.subplot.plot(self.historic)
        self.subplot.set(ylabel="Volts", autoscalex_on=False, xlim=(0, self.nbpoints), autoscaley_on=False, ylim=(-0.1, 5.2))
        self.canvas.draw()

#-----------------------------------------------------------------------------------------------------------------------
# ===Done===  fullfill this class
class PeakPlot:
    def __init__(self, root, canvas, nbpoints):
        self.nbpoints : int   = nbpoints
        self.historic : float = []
        self.peak_historic = []
        self.new_peaks = []

        fig = Figure(dpi=100)
        fig.set_tight_layout({"pad" : 1})
        self.subplot = fig.add_subplot()
        
        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().place(in_=canvas, relwidth=1, relheight=1)
    
    def NewPeaksDetect(self):
        tmp_peaks = self.new_peaks
        self.new_peaks = []
        for peak in tmp_peaks:
            self.peak_historic.append(peak)

        return tmp_peaks
        
    def PeakDetect(self, Min, Delta, Width):
        TabPos    : int   = []
        TabHeight : float = []
        for i in range(1, len(self.historic)):
            if self.historic[i] - self.historic[max(0, i - int(Width/2))] >= Delta and (i + int(Width/2)) < len(self.historic):
                    if self.historic[i+int(Width/2)] - self.historic[i] <= Delta:
                        max_i = self.historic.index(max(self.historic[i:i+Width]))
                        if self.historic[max_i] < Min:
                            continue
                        TabPos.append(max_i)
                        TabHeight.append(self.historic[max_i])
                        if not (max_i + 1, self.historic[max_i]) in self.peak_historic or not (max_i + 1, self.historic[max_i]) in self.new_peaks:
                            self.new_peaks.append((max_i, self.historic[max_i]))

        return TabPos, TabHeight

    def Plot(self, t:datetime, v:float, d:str):
        if len(self.historic) >= self.nbpoints:
            self.historic.pop(0)

        self.historic.append(v)
        self.peak_pos, self.peak_height = self.PeakDetect(10, 1, 3)
        print(self.peak_pos, self.peak_height)
        self.subplot.clear()
        self.subplot.plot(self.historic)
        self.subplot.scatter(self.peak_pos, self.peak_height, color = 'r', s = 50, marker = 'D', label = 'Peaks')
        self.subplot.set(ylabel="Km/h", autoscalex_on=False, xlim=(0, self.nbpoints), autoscaley_on=False, ylim=(-0.1, max(30, max(self.historic))))
        self.subplot.legend()
        self.canvas.draw()

        return str(t + " - " + "{:.1f}".format(v) + " - " + d + "\n")


#-----------------------------------------------------------------------------------------------------------------------
