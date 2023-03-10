#############################################################################
# Generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#  Jan 17, 2023 12:00:23 PM CET  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {Courier New} -size 10"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_treeview_desc) $desc
set vTcl(actual_gui_font_treeview_name) [font create {*}$desc]
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 269x260+983+180
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2110 1418
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    set toptitle "Min/Max Values"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "MinMaxWin" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    labelframe $top.lab47 \
        \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground black -text {Mesures physiques} \
        -background $vTcl(actual_gui_bg) -height 405 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 580 
    vTcl:DefineAlias "$top.lab47" "FramePMes" vTcl:WidgetProc "MinMaxWin" 1
    set site_3_0 $top.lab47
    message $site_3_0.mes79 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Vitesse vent} -width 80 
    vTcl:DefineAlias "$site_3_0.mes79" "MsgPVitVent" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab81 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 0 
    vTcl:DefineAlias "$site_3_0.lab81" "MinVitVent" vTcl:WidgetProc "MinMaxWin" 1
    message $site_3_0.mes82 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Temperature -width 80 
    vTcl:DefineAlias "$site_3_0.mes82" "MsgPTemperature" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab83 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {9,999 V} 
    vTcl:DefineAlias "$site_3_0.lab83" "MinTemperature" vTcl:WidgetProc "MinMaxWin" 1
    message $site_3_0.mes84 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Luminosit?? -width 70 
    vTcl:DefineAlias "$site_3_0.mes84" "MsgPLuminosite" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab85 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {9,999 V} 
    vTcl:DefineAlias "$site_3_0.lab85" "MinLuminosite" vTcl:WidgetProc "MinMaxWin" 1
    message $site_3_0.mes87 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Humidit?? -width 60 
    vTcl:DefineAlias "$site_3_0.mes87" "MsgPHumidite" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab88 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {999 Hz} 
    vTcl:DefineAlias "$site_3_0.lab88" "MinHumidite" vTcl:WidgetProc "MinMaxWin" 1
    message $site_3_0.mes89 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Pluviom??trie -width 80 
    vTcl:DefineAlias "$site_3_0.mes89" "MsgPPluviometrie" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab90 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 0 
    vTcl:DefineAlias "$site_3_0.lab90" "MinPluviometrie" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe47 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe47" "TSeparator1" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe48 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe48" "TSeparator2" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe49 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe49" "TSeparator3" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab52 \
        -activeforeground SystemButtonText -background $vTcl(actual_gui_bg) \
        -compound left -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$site_3_0.lab52" "MaxVitVent" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab54 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$site_3_0.lab54" "Label1_1" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab55 \
        -activeforeground #000000 -background $vTcl(actual_gui_bg) \
        -compound left -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Label 
    vTcl:DefineAlias "$site_3_0.lab55" "MaxTemperature" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab56 \
        -activeforeground SystemButtonText -background $vTcl(actual_gui_bg) \
        -compound left -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$site_3_0.lab56" "MaxLuminosite" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab57 \
        -activeforeground SystemButtonText -background $vTcl(actual_gui_bg) \
        -compound left -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$site_3_0.lab57" "MaxHumidite" vTcl:WidgetProc "MinMaxWin" 1
    label $site_3_0.lab58 \
        -activeforeground SystemButtonText -background $vTcl(actual_gui_bg) \
        -compound left -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$site_3_0.lab58" "MaxPluviometrie" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe59
    vTcl:DefineAlias "$site_3_0.tSe59" "TSeparator4" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe60 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe60" "TSeparator5" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe61
    vTcl:DefineAlias "$site_3_0.tSe61" "TSeparator6" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe62
    vTcl:DefineAlias "$site_3_0.tSe62" "TSeparator7" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe63
    vTcl:DefineAlias "$site_3_0.tSe63" "TSeparator8" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe64
    vTcl:DefineAlias "$site_3_0.tSe64" "TSeparator9" vTcl:WidgetProc "MinMaxWin" 1
    message $site_3_0.mes65 \
        -background $vTcl(actual_gui_bg) -font {-family {Segoe UI} -size 9} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -padx 1 -pady 1 -text Mesure -width 60 
    vTcl:DefineAlias "$site_3_0.mes65" "Message1" vTcl:WidgetProc "MinMaxWin" 1
    message $site_3_0.mes66 \
        -background $vTcl(actual_gui_bg) -font {-family {Segoe UI} -size 9} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -padx 1 -pady 1 -text Minimum -width 60 
    vTcl:DefineAlias "$site_3_0.mes66" "Message2" vTcl:WidgetProc "MinMaxWin" 1
    message $site_3_0.mes67 \
        -background $vTcl(actual_gui_bg) -font {-family {Segoe UI} -size 9} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -padx 1 -pady 1 -text Maximum -width 60 
    vTcl:DefineAlias "$site_3_0.mes67" "Message3" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe68
    vTcl:DefineAlias "$site_3_0.tSe68" "TSeparator10" vTcl:WidgetProc "MinMaxWin" 1
    ttk::separator $site_3_0.tSe69
    vTcl:DefineAlias "$site_3_0.tSe69" "TSeparator11" vTcl:WidgetProc "MinMaxWin" 1
    place $site_3_0.mes79 \
        -in $site_3_0 -x 10 -y 70 -width 80 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab81 \
        -in $site_3_0 -x 110 -y 70 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes82 \
        -in $site_3_0 -x 19 -y 110 -width 80 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab83 \
        -in $site_3_0 -x 110 -y 110 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes84 \
        -in $site_3_0 -x 25 -y 150 -width 70 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab85 \
        -in $site_3_0 -x 110 -y 150 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes87 \
        -in $site_3_0 -x 30 -y 190 -width 60 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab88 \
        -in $site_3_0 -x 110 -y 190 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes89 \
        -in $site_3_0 -x 20 -y 230 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab90 \
        -in $site_3_0 -x 110 -y 230 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSe47 \
        -in $site_3_0 -x 0 -relx 0.173 -y 0 -rely 0.096 -height 0 \
        -relheight 0.543 -anchor nw -bordermode ignore 
    place $site_3_0.tSe48 \
        -in $site_3_0 -x 0 -relx 0.308 -y 0 -rely 0.096 -height 0 \
        -relheight 0.543 -anchor nw -bordermode ignore 
    place $site_3_0.tSe49 \
        -in $site_3_0 -x 0 -relx 0.444 -y 0 -rely 0.096 -height 0 \
        -relheight 0.543 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 190 -y 70 -width 64 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 144 -y 440 -width 64 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 190 -y 110 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 190 -y 150 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 190 -y 190 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab58 \
        -in $site_3_0 -x 190 -y 230 -width 64 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSe59 \
        -in $site_3_0 -x 0 -relx 0.02 -y 0 -rely 0.244 -width 0 \
        -relwidth 0.424 -anchor nw -bordermode ignore 
    place $site_3_0.tSe60 \
        -in $site_3_0 -x 0 -relx 0.02 -y 0 -rely 0.096 -height 0 \
        -relheight 0.543 -anchor nw -bordermode ignore 
    place $site_3_0.tSe61 \
        -in $site_3_0 -x 0 -relx 0.02 -y 0 -rely 0.343 -width 0 \
        -relwidth 0.424 -anchor nw -bordermode ignore 
    place $site_3_0.tSe62 \
        -in $site_3_0 -x 0 -relx 0.02 -y 0 -rely 0.442 -width 0 \
        -relwidth 0.424 -anchor nw -bordermode ignore 
    place $site_3_0.tSe63 \
        -in $site_3_0 -x 0 -relx 0.02 -y 0 -rely 0.541 -width 0 \
        -relwidth 0.424 -anchor nw -bordermode ignore 
    place $site_3_0.tSe64 \
        -in $site_3_0 -x 0 -relx 0.02 -y 0 -rely 0.64 -width 0 \
        -relwidth 0.424 -anchor nw -bordermode ignore 
    place $site_3_0.mes65 \
        -in $site_3_0 -x 30 -y 40 -anchor nw -bordermode ignore 
    place $site_3_0.mes66 \
        -in $site_3_0 -x 110 -y 40 -anchor nw -bordermode ignore 
    place $site_3_0.mes67 \
        -in $site_3_0 -x 190 -y 40 -width 60 -relwidth 0 -height 19 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSe68 \
        -in $site_3_0 -x 0 -relx 0.02 -y 61 -width 0 -relwidth 0.424 \
        -anchor nw -bordermode ignore 
    place $site_3_0.tSe69 \
        -in $site_3_0 -x 0 -relx 0.02 -y 37 -width 0 -relwidth 0.424 \
        -anchor nw -bordermode ignore 
    menu $top.m46 \
        -activebackground #c0c0c0 -activeforeground $vTcl(actual_gui_fg) \
        -background $vTcl(actual_gui_menu_bg) \
        -font $vTcl(actual_gui_font_menu_desc) -foreground #c0c0c0 -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab47 \
        -in $top -x 0 -y -30 -width 580 -relwidth 0 -height 405 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

