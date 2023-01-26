#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpGUIGraph - Helper for plotting Graph & Chart on GUI                              JYC-2022
#-----------------------------------------------------------------------------------------------------------------------

from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
# ===ToDo===  fullfill this class
def PeakDetect(Values, Delta):
    TabPos : int = []
    TabHeight : float = []
    TabPos.append(30); TabHeight.append(Values[30])
    TabPos.append(60); TabHeight.append(Values[60])

    return TabPos, TabHeight

class PeakPlot:
    def __init__(self, root, canvas, nbpoints):
        pass

    def Plot(self, t:datetime, v:float, d:str):
        pass
        # fig = plt.figure("Plotting peak detection")
        # ax = fig.subplots()

        # ax.plot(x,y)
        # ax.scatter(peak_pos, peak_height, color = 'r', s = 50, marker = 'D', label = 'Peaks')
        # ax.legend()
        # ax.grid()

        # plt.show()


#-----------------------------------------------------------------------------------------------------------------------
