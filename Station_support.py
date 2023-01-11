#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - Support - GUI events manager                                                        JYC-2022
#-----------------------------------------------------------------------------------------------------------------------

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Station
from Station_share import GUICenter, GUIUpdate, EMes

#-- Custom part ----------------------------------------------------------------
def GUIRefresh():
    global root, _w1
    GUIUpdate(root, _w1)
    root.after(200, GUIRefresh)                                # run every 200ms

def BtnPlvResetEvt(*args):
    EMes.Girouette   = 0   
    EMes.Anemometre  = 0
    EMes.Thermometre = 0
    EMes.Luxmetre    = 0
    EMes.Humidimetre = 0
    EMes.Pluviometre = 0
    EMes.Encodeur    = 0
    EMes.DureeMesures= 0
    EMes.TempsBoucleR= 0
    EMes.TempsBoucleL= 0

#-------------------------------------------------------------------------------

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Station.MainWin(_top1)
    #-- Custom part ------------------------------------------------------------
    _top1.resizable(0, 0)
    GUICenter(_top1)
    GUIRefresh()
    #---------------------------------------------------------------------------
    root.mainloop()

if __name__ == '__main__':
    Station.start_up()
