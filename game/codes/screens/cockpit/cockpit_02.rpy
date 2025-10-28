screen cockpit_02:
    imagebutton:
        idle "rock_cock.png"
        hover "rock_cock_hover.png"
        xanchor -253
        yanchor -15
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Pick Up Item_sfx.mp3"),Jump("arc_2")
    imagebutton:
        idle "fud_can_idle.png"
        hover "fud_can.png"
        xanchor 651
        yanchor -120
        xpos 0.5
        ypos 0.28
        action Jump("can_f")
    imagebutton:
        idle "radio_idle.png"
        hover "radio.png"
        xanchor -67
        yanchor 224
        xpos 0.5
        ypos 0.28
        action Jump("radio_f")
    imagebutton:
        idle "wall_et_idle.png"
        hover "wall_et.png"
        xanchor 480
        yanchor -210
        xpos 0.5
        ypos 0.28
        action Jump("wallet_f")
    imagebutton:
        idle "buck_trush_idle.png"
        hover "buck_trush.png"
        xanchor 254
        yanchor -260
        xpos 0.5
        ypos 0.28
        action Jump("plastic_f")
    imagebutton:
        idle "notde1_idle.png"
        hover "notde1.png"
        xanchor -395
        yanchor 156
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Paper_sfx.wav"), Jump("note_1_f")
    imagebutton:
        idle "notde2_idle.png"
        hover "notde2.png"
        xanchor 275
        yanchor 146
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Paper_sfx.wav"), Jump("note_2")
       