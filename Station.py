#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Dec 01, 2022 07:28:34 PM CET  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import Station_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 
font9 = "-family {Segoe UI} -size 9"

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='-family {Segoe UI} -size 9')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class MainWin:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("519x467+272+102")
        top.minsize(120, 1)
        top.maxsize(2110, 1418)
        top.resizable(1,  1)
        top.title("Station météo")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.FrameEtat = tk.Frame(self.top)
        self.FrameEtat.place(relx=0.0, rely=0.942, relheight=0.054
                , relwidth=0.992)
        self.FrameEtat.configure(relief='sunken')
        self.FrameEtat.configure(borderwidth="2")
        self.FrameEtat.configure(relief="sunken")
        self.FrameEtat.configure(background="#d9d9d9")
        self.FrameEtat.configure(highlightbackground="#d9d9d9")
        self.FrameEtat.configure(highlightcolor="black")

        self.MsgEtat = tk.Message(self.FrameEtat)
        self.MsgEtat.place(relx=0.006, rely=0.08, relheight=0.84, relwidth=0.078)

        self.MsgEtat.configure(background="#d9d9d9")
        self.MsgEtat.configure(font="-family {Segoe UI} -size 9")
        self.MsgEtat.configure(foreground="#000000")
        self.MsgEtat.configure(highlightbackground="#d9d9d9")
        self.MsgEtat.configure(highlightcolor="black")
        self.MsgEtat.configure(text='''État :''')
        self.MsgEtat.configure(width=60)

        self.Etat = tk.Label(self.FrameEtat)
        self.Etat.place(relx=0.078, rely=0.16, height=17, width=468)
        self.Etat.configure(activebackground="#f9f9f9")
        self.Etat.configure(activeforeground="black")
        self.Etat.configure(anchor='w')
        self.Etat.configure(background="#d9d9d9")
        self.Etat.configure(disabledforeground="#a3a3a3")
        self.Etat.configure(font="-family {Segoe UI} -size 9")
        self.Etat.configure(foreground="#000000")
        self.Etat.configure(highlightbackground="#d9d9d9")
        self.Etat.configure(highlightcolor="black")
        self.Etat.configure(text='''Mesures en cours ...''')

        self.FrameEMes = tk.LabelFrame(self.top)
        self.FrameEMes.place(relx=0.019, rely=0.021, relheight=0.867
                , relwidth=0.963)
        self.FrameEMes.configure(relief='groove')
        self.FrameEMes.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.FrameEMes.configure(foreground="black")
        self.FrameEMes.configure(text='''Mesures électriques''')
        self.FrameEMes.configure(background="#d9d9d9")
        self.FrameEMes.configure(highlightbackground="#d9d9d9")
        self.FrameEMes.configure(highlightcolor="black")

        self.MsgEGirouette = tk.Message(self.FrameEMes)
        self.MsgEGirouette.place(relx=0.04, rely=0.074, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEGirouette.configure(anchor='e')
        self.MsgEGirouette.configure(background="#d9d9d9")
        self.MsgEGirouette.configure(font="-family {Segoe UI} -size 9")
        self.MsgEGirouette.configure(foreground="#000000")
        self.MsgEGirouette.configure(highlightbackground="#d9d9d9")
        self.MsgEGirouette.configure(highlightcolor="black")
        self.MsgEGirouette.configure(text='''Girouette''')
        self.MsgEGirouette.configure(width=80)

        self.EGirouette = tk.Label(self.FrameEMes)
        self.EGirouette.place(relx=0.2, rely=0.074, height=21, width=54
                , bordermode='ignore')
        self.EGirouette.configure(activebackground="#f9f9f9")
        self.EGirouette.configure(activeforeground="black")
        self.EGirouette.configure(anchor='e')
        self.EGirouette.configure(background="#d9d9d9")
        self.EGirouette.configure(disabledforeground="#a3a3a3")
        self.EGirouette.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EGirouette.configure(foreground="#000000")
        self.EGirouette.configure(highlightbackground="#d9d9d9")
        self.EGirouette.configure(highlightcolor="black")
        self.EGirouette.configure(relief="sunken")
        self.EGirouette.configure(text='''9,999 V''')

        self.MsgEAnemometre = tk.Message(self.FrameEMes)
        self.MsgEAnemometre.place(relx=0.04, rely=0.173, relheight=0.057
                , relwidth=0.16, bordermode='ignore')
        self.MsgEAnemometre.configure(anchor='e')
        self.MsgEAnemometre.configure(background="#d9d9d9")
        self.MsgEAnemometre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEAnemometre.configure(foreground="#000000")
        self.MsgEAnemometre.configure(highlightbackground="#d9d9d9")
        self.MsgEAnemometre.configure(highlightcolor="black")
        self.MsgEAnemometre.configure(text='''Anémomètre''')
        self.MsgEAnemometre.configure(width=80)

        self.EAnemometre = tk.Label(self.FrameEMes)
        self.EAnemometre.place(relx=0.2, rely=0.173, height=21, width=54
                , bordermode='ignore')
        self.EAnemometre.configure(activebackground="#f9f9f9")
        self.EAnemometre.configure(activeforeground="black")
        self.EAnemometre.configure(anchor='e')
        self.EAnemometre.configure(background="#d9d9d9")
        self.EAnemometre.configure(disabledforeground="#a3a3a3")
        self.EAnemometre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EAnemometre.configure(foreground="#000000")
        self.EAnemometre.configure(highlightbackground="#d9d9d9")
        self.EAnemometre.configure(highlightcolor="black")
        self.EAnemometre.configure(relief="sunken")
        self.EAnemometre.configure(text='''0''')

        self.MsgEThermometre = tk.Message(self.FrameEMes)
        self.MsgEThermometre.place(relx=0.04, rely=0.272, relheight=0.057
                , relwidth=0.16, bordermode='ignore')
        self.MsgEThermometre.configure(anchor='e')
        self.MsgEThermometre.configure(background="#d9d9d9")
        self.MsgEThermometre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEThermometre.configure(foreground="#000000")
        self.MsgEThermometre.configure(highlightbackground="#d9d9d9")
        self.MsgEThermometre.configure(highlightcolor="black")
        self.MsgEThermometre.configure(text='''Thermomètre''')
        self.MsgEThermometre.configure(width=80)

        self.EThermometre = tk.Label(self.FrameEMes)
        self.EThermometre.place(relx=0.2, rely=0.272, height=21, width=54
                , bordermode='ignore')
        self.EThermometre.configure(activebackground="#f9f9f9")
        self.EThermometre.configure(activeforeground="black")
        self.EThermometre.configure(anchor='e')
        self.EThermometre.configure(background="#d9d9d9")
        self.EThermometre.configure(disabledforeground="#a3a3a3")
        self.EThermometre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EThermometre.configure(foreground="#000000")
        self.EThermometre.configure(highlightbackground="#d9d9d9")
        self.EThermometre.configure(highlightcolor="black")
        self.EThermometre.configure(relief="sunken")
        self.EThermometre.configure(text='''9,999 V''')

        self.MsgELuxmetre = tk.Message(self.FrameEMes)
        self.MsgELuxmetre.place(relx=0.04, rely=0.37, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgELuxmetre.configure(anchor='e')
        self.MsgELuxmetre.configure(background="#d9d9d9")
        self.MsgELuxmetre.configure(font="-family {Segoe UI} -size 9")
        self.MsgELuxmetre.configure(foreground="#000000")
        self.MsgELuxmetre.configure(highlightbackground="#d9d9d9")
        self.MsgELuxmetre.configure(highlightcolor="black")
        self.MsgELuxmetre.configure(text='''Luxmètre''')
        self.MsgELuxmetre.configure(width=80)

        self.ELuxmetre = tk.Label(self.FrameEMes)
        self.ELuxmetre.place(relx=0.2, rely=0.37, height=21, width=54
                , bordermode='ignore')
        self.ELuxmetre.configure(activebackground="#f9f9f9")
        self.ELuxmetre.configure(activeforeground="black")
        self.ELuxmetre.configure(anchor='e')
        self.ELuxmetre.configure(background="#d9d9d9")
        self.ELuxmetre.configure(disabledforeground="#a3a3a3")
        self.ELuxmetre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.ELuxmetre.configure(foreground="#000000")
        self.ELuxmetre.configure(highlightbackground="#d9d9d9")
        self.ELuxmetre.configure(highlightcolor="black")
        self.ELuxmetre.configure(relief="sunken")
        self.ELuxmetre.configure(text='''9,999 V''')

        self.MsgEHumidimetre = tk.Message(self.FrameEMes)
        self.MsgEHumidimetre.place(relx=0.04, rely=0.469, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEHumidimetre.configure(anchor='e')
        self.MsgEHumidimetre.configure(background="#d9d9d9")
        self.MsgEHumidimetre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEHumidimetre.configure(foreground="#000000")
        self.MsgEHumidimetre.configure(highlightbackground="#d9d9d9")
        self.MsgEHumidimetre.configure(highlightcolor="black")
        self.MsgEHumidimetre.configure(text='''Humidimètre''')
        self.MsgEHumidimetre.configure(width=80)

        self.EHumidimetre = tk.Label(self.FrameEMes)
        self.EHumidimetre.place(relx=0.2, rely=0.469, height=21, width=54
                , bordermode='ignore')
        self.EHumidimetre.configure(activebackground="#f9f9f9")
        self.EHumidimetre.configure(activeforeground="black")
        self.EHumidimetre.configure(anchor='e')
        self.EHumidimetre.configure(background="#d9d9d9")
        self.EHumidimetre.configure(disabledforeground="#a3a3a3")
        self.EHumidimetre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EHumidimetre.configure(foreground="#000000")
        self.EHumidimetre.configure(highlightbackground="#d9d9d9")
        self.EHumidimetre.configure(highlightcolor="black")
        self.EHumidimetre.configure(relief="sunken")
        self.EHumidimetre.configure(text='''999 Hz''')

        self.MsgEPluviometre = tk.Message(self.FrameEMes)
        self.MsgEPluviometre.place(relx=0.04, rely=0.568, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEPluviometre.configure(anchor='e')
        self.MsgEPluviometre.configure(background="#d9d9d9")
        self.MsgEPluviometre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEPluviometre.configure(foreground="#000000")
        self.MsgEPluviometre.configure(highlightbackground="#d9d9d9")
        self.MsgEPluviometre.configure(highlightcolor="black")
        self.MsgEPluviometre.configure(text='''Pluviomètre''')
        self.MsgEPluviometre.configure(width=80)

        self.EPluviometre = tk.Label(self.FrameEMes)
        self.EPluviometre.place(relx=0.2, rely=0.568, height=21, width=54
                , bordermode='ignore')
        self.EPluviometre.configure(activebackground="#f9f9f9")
        self.EPluviometre.configure(activeforeground="black")
        self.EPluviometre.configure(anchor='e')
        self.EPluviometre.configure(background="#d9d9d9")
        self.EPluviometre.configure(disabledforeground="#a3a3a3")
        self.EPluviometre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EPluviometre.configure(foreground="#000000")
        self.EPluviometre.configure(highlightbackground="#d9d9d9")
        self.EPluviometre.configure(highlightcolor="black")
        self.EPluviometre.configure(relief="sunken")
        self.EPluviometre.configure(text='''0''')

        _style_code()
        self.BtnPlvReset = ttk.Button(self.FrameEMes)
        self.BtnPlvReset.place(relx=0.312, rely=0.563, height=25, width=26
                , bordermode='ignore')
        self.BtnPlvReset.configure(takefocus="")
        self.BtnPlvReset.configure(text='''0''')
        self.BtnPlvReset.bind('<ButtonRelease-1>',lambda e:Station_support.BtnPlvResetEvt(e))

        self.MsgEEncodeur = tk.Message(self.FrameEMes)
        self.MsgEEncodeur.place(relx=0.04, rely=0.667, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEEncodeur.configure(anchor='e')
        self.MsgEEncodeur.configure(background="#d9d9d9")
        self.MsgEEncodeur.configure(font="-family {Segoe UI} -size 9")
        self.MsgEEncodeur.configure(foreground="#000000")
        self.MsgEEncodeur.configure(highlightbackground="#d9d9d9")
        self.MsgEEncodeur.configure(highlightcolor="black")
        self.MsgEEncodeur.configure(text='''Encodeur''')
        self.MsgEEncodeur.configure(width=80)

        self.EEncodeur = tk.Label(self.FrameEMes)
        self.EEncodeur.place(relx=0.2, rely=0.667, height=21, width=54
                , bordermode='ignore')
        self.EEncodeur.configure(activebackground="#f9f9f9")
        self.EEncodeur.configure(activeforeground="black")
        self.EEncodeur.configure(anchor='e')
        self.EEncodeur.configure(background="#d9d9d9")
        self.EEncodeur.configure(disabledforeground="#a3a3a3")
        self.EEncodeur.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EEncodeur.configure(foreground="#000000")
        self.EEncodeur.configure(highlightbackground="#d9d9d9")
        self.EEncodeur.configure(highlightcolor="black")
        self.EEncodeur.configure(relief="sunken")
        self.EEncodeur.configure(text='''0''')

        self.EP1_0 = tk.Label(self.FrameEMes)
        self.EP1_0.place(relx=0.37, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_0.configure(activebackground="#f9f9f9")
        self.EP1_0.configure(activeforeground="black")
        self.EP1_0.configure(background="#d9d9d9")
        self.EP1_0.configure(disabledforeground="#a3a3a3")
        self.EP1_0.configure(font="-family {Segoe UI} -size 9")
        self.EP1_0.configure(foreground="#000000")
        self.EP1_0.configure(highlightbackground="#d9d9d9")
        self.EP1_0.configure(highlightcolor="black")
        self.EP1_0.configure(relief="raised")

        self.EP1_3 = tk.Label(self.FrameEMes)
        self.EP1_3.place(relx=0.31, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_3.configure(activebackground="#f9f9f9")
        self.EP1_3.configure(activeforeground="black")
        self.EP1_3.configure(background="#d9d9d9")
        self.EP1_3.configure(disabledforeground="#a3a3a3")
        self.EP1_3.configure(font="-family {Segoe UI} -size 9")
        self.EP1_3.configure(foreground="#000000")
        self.EP1_3.configure(highlightbackground="#d9d9d9")
        self.EP1_3.configure(highlightcolor="black")
        self.EP1_3.configure(relief="raised")

        self.EP1_2 = tk.Label(self.FrameEMes)
        self.EP1_2.place(relx=0.33, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_2.configure(activebackground="#f9f9f9")
        self.EP1_2.configure(activeforeground="black")
        self.EP1_2.configure(background="#d9d9d9")
        self.EP1_2.configure(disabledforeground="#a3a3a3")
        self.EP1_2.configure(font="-family {Segoe UI} -size 9")
        self.EP1_2.configure(foreground="#000000")
        self.EP1_2.configure(highlightbackground="#d9d9d9")
        self.EP1_2.configure(highlightcolor="black")
        self.EP1_2.configure(relief="raised")

        self.EP1_1 = tk.Label(self.FrameEMes)
        self.EP1_1.place(relx=0.35, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_1.configure(activebackground="#f9f9f9")
        self.EP1_1.configure(activeforeground="black")
        self.EP1_1.configure(background="#d9d9d9")
        self.EP1_1.configure(disabledforeground="#a3a3a3")
        self.EP1_1.configure(font="-family {Segoe UI} -size 9")
        self.EP1_1.configure(foreground="#000000")
        self.EP1_1.configure(highlightbackground="#d9d9d9")
        self.EP1_1.configure(highlightcolor="black")
        self.EP1_1.configure(relief="raised")

        self.MsgEDureeMesures = tk.Message(self.FrameEMes)
        self.MsgEDureeMesures.place(relx=0.02, rely=0.765, relheight=0.057
                , relwidth=0.18, bordermode='ignore')
        self.MsgEDureeMesures.configure(anchor='e')
        self.MsgEDureeMesures.configure(background="#d9d9d9")
        self.MsgEDureeMesures.configure(font="-family {Segoe UI} -size 9")
        self.MsgEDureeMesures.configure(foreground="#000000")
        self.MsgEDureeMesures.configure(highlightbackground="#d9d9d9")
        self.MsgEDureeMesures.configure(highlightcolor="black")
        self.MsgEDureeMesures.configure(text='''Durée mesures''')
        self.MsgEDureeMesures.configure(width=90)

        self.EDureeMesures = tk.Label(self.FrameEMes)
        self.EDureeMesures.place(relx=0.2, rely=0.765, height=21, width=54
                , bordermode='ignore')
        self.EDureeMesures.configure(activebackground="#f9f9f9")
        self.EDureeMesures.configure(activeforeground="black")
        self.EDureeMesures.configure(anchor='e')
        self.EDureeMesures.configure(background="#d9d9d9")
        self.EDureeMesures.configure(disabledforeground="#a3a3a3")
        self.EDureeMesures.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EDureeMesures.configure(foreground="#000000")
        self.EDureeMesures.configure(highlightbackground="#d9d9d9")
        self.EDureeMesures.configure(highlightcolor="black")
        self.EDureeMesures.configure(relief="sunken")
        self.EDureeMesures.configure(text='''9999 ms''')

        self.MsgETempsBoucleR = tk.Message(self.FrameEMes)
        self.MsgETempsBoucleR.place(relx=0.02, rely=0.914, relheight=0.057
                , relwidth=0.28, bordermode='ignore')
        self.MsgETempsBoucleR.configure(anchor='e')
        self.MsgETempsBoucleR.configure(background="#d9d9d9")
        self.MsgETempsBoucleR.configure(font="-family {Segoe UI} -size 9")
        self.MsgETempsBoucleR.configure(foreground="#000000")
        self.MsgETempsBoucleR.configure(highlightbackground="#d9d9d9")
        self.MsgETempsBoucleR.configure(highlightcolor="black")
        self.MsgETempsBoucleR.configure(text='''Temps de boucle rapide''')
        self.MsgETempsBoucleR.configure(width=140)

        self.ETempsBoucleR = tk.Label(self.FrameEMes)
        self.ETempsBoucleR.place(relx=0.3, rely=0.914, height=21, width=54
                , bordermode='ignore')
        self.ETempsBoucleR.configure(activebackground="#f9f9f9")
        self.ETempsBoucleR.configure(activeforeground="black")
        self.ETempsBoucleR.configure(anchor='e')
        self.ETempsBoucleR.configure(background="#d9d9d9")
        self.ETempsBoucleR.configure(disabledforeground="#a3a3a3")
        self.ETempsBoucleR.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.ETempsBoucleR.configure(foreground="#000000")
        self.ETempsBoucleR.configure(highlightbackground="#d9d9d9")
        self.ETempsBoucleR.configure(highlightcolor="black")
        self.ETempsBoucleR.configure(relief="sunken")
        self.ETempsBoucleR.configure(text='''9999 ms''')

        self.MsgETempsBoucleL = tk.Message(self.FrameEMes)
        self.MsgETempsBoucleL.place(relx=0.56, rely=0.914, relheight=0.057
                , relwidth=0.28, bordermode='ignore')
        self.MsgETempsBoucleL.configure(anchor='e')
        self.MsgETempsBoucleL.configure(background="#d9d9d9")
        self.MsgETempsBoucleL.configure(font="-family {Segoe UI} -size 9")
        self.MsgETempsBoucleL.configure(foreground="#000000")
        self.MsgETempsBoucleL.configure(highlightbackground="#d9d9d9")
        self.MsgETempsBoucleL.configure(highlightcolor="black")
        self.MsgETempsBoucleL.configure(text='''Temps de boucle lente''')
        self.MsgETempsBoucleL.configure(width=140)

        self.ETempsBoucleL = tk.Label(self.FrameEMes)
        self.ETempsBoucleL.place(relx=0.84, rely=0.914, height=21, width=54
                , bordermode='ignore')
        self.ETempsBoucleL.configure(activebackground="#f9f9f9")
        self.ETempsBoucleL.configure(activeforeground="black")
        self.ETempsBoucleL.configure(anchor='e')
        self.ETempsBoucleL.configure(background="#d9d9d9")
        self.ETempsBoucleL.configure(disabledforeground="#a3a3a3")
        self.ETempsBoucleL.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.ETempsBoucleL.configure(foreground="#000000")
        self.ETempsBoucleL.configure(highlightbackground="#d9d9d9")
        self.ETempsBoucleL.configure(highlightcolor="black")
        self.ETempsBoucleL.configure(relief="sunken")
        self.ETempsBoucleL.configure(text='''9999 ms''')

        self.EChartGirouette = tk.Canvas(self.FrameEMes)
        self.EChartGirouette.place(relx=0.46, rely=0.074, relheight=0.353
                , relwidth=0.506, bordermode='ignore')
        self.EChartGirouette.configure(background="#ffffff")
        self.EChartGirouette.configure(borderwidth="2")
        self.EChartGirouette.configure(highlightbackground="#d9d9d9")
        self.EChartGirouette.configure(highlightcolor="black")
        self.EChartGirouette.configure(insertbackground="black")
        self.EChartGirouette.configure(selectbackground="blue")
        self.EChartGirouette.configure(selectforeground="white")

        self.EGraphHumidite = tk.Canvas(self.FrameEMes)
        self.EGraphHumidite.place(relx=0.46, rely=0.469, relheight=0.353
                , relwidth=0.506, bordermode='ignore')
        self.EGraphHumidite.configure(background="#ffffff")
        self.EGraphHumidite.configure(borderwidth="2")
        self.EGraphHumidite.configure(highlightbackground="#d9d9d9")
        self.EGraphHumidite.configure(highlightcolor="black")
        self.EGraphHumidite.configure(insertbackground="black")
        self.EGraphHumidite.configure(selectbackground="blue")
        self.EGraphHumidite.configure(selectforeground="white")

        self.Msg1 = tk.Message(self.FrameEMes)
        self.Msg1.place(relx=0.32, rely=0.074, relheight=0.057, relwidth=0.122
                , bordermode='ignore')
        self.Msg1.configure(anchor='w')
        self.Msg1.configure(background="#d9d9d9")
        self.Msg1.configure(font="-family {Segoe UI} -size 9")
        self.Msg1.configure(foreground="#000000")
        self.Msg1.configure(highlightbackground="#d9d9d9")
        self.Msg1.configure(highlightcolor="black")
        self.Msg1.configure(text='''>>>>>>''')
        self.Msg1.configure(width=61)

        self.Msg2 = tk.Message(self.FrameEMes)
        self.Msg2.place(relx=0.32, rely=0.469, relheight=0.057, relwidth=0.122
                , bordermode='ignore')
        self.Msg2.configure(anchor='w')
        self.Msg2.configure(background="#d9d9d9")
        self.Msg2.configure(font="-family {Segoe UI} -size 9")
        self.Msg2.configure(foreground="#000000")
        self.Msg2.configure(highlightbackground="#d9d9d9")
        self.Msg2.configure(highlightcolor="black")
        self.Msg2.configure(text='''>>>>>>''')
        self.Msg2.configure(width=61)

def start_up():
    Station_support.main()

if __name__ == '__main__':
    Station_support.main()




