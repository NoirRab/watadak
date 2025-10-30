default fatimah_photo_collected = False

screen cockpit:
    imagebutton:
        idle "rock_cock.png"
        hover "rock_cock_hover.png"
        xanchor -253
        yanchor -15
        xpos 0.5
        ypos 0.28
        action [
            Play("sound", "audio/Pick Up Item_sfx.mp3"), 
            Hide("cockpit"), Call("cigarettes")
            ]
    imagebutton:
        idle "fud_can_idle.png"
        hover "fud_can.png"
        xanchor 651
        yanchor -120
        xpos 0.5
        ypos 0.28
        action Call("can")
    imagebutton:
        idle "wall_et_idle.png"
        hover "wall_et.png"
        xanchor 480
        yanchor -210
        xpos 0.5
        ypos 0.28
        action Call("wallet")
    imagebutton:
        idle "buck_trush_idle.png"
        hover "buck_trush.png"
        xanchor 254
        yanchor -260
        xpos 0.5
        ypos 0.28
        action Call("plastic")
    imagebutton:
        idle "notde1_idle.png"
        hover "notde1.png"
        xanchor -395
        yanchor 156
        xpos 0.5
        ypos 0.28
        action [
            Play("sound", "audio/Paper_sfx.wav"), 
            Call("note_1")
            ]
    imagebutton:
        idle "radio_idle.png"
        hover "radio.png"
        xanchor -67
        yanchor 224
        xpos 0.5
        ypos 0.28
        action Call("radio")
    imagebutton:
        idle "notde2_idle.png"
        hover "notde2.png"
        xanchor 275
        yanchor 146
        xpos 0.5
        ypos 0.28
        action [
            Play("sound", "audio/Paper_sfx.wav"), 
            Call("note_2")
            ]
    if not fatimah_photo_collected:
        imagebutton:
            idle "keluar_ga_pict_01_idle.png"
            hover "keluar_ga_pict_01.png"
            xanchor 170
            yanchor 112
            xpos 0.5
            ypos 0.28
            sensitive not fatimah_photo_collected
            action [
                SetVariable("fatimah_photo_collected", True),
                Play("sound", "audio/Pick Up Item_sfx.mp3"),
                Call("fatimah_image")
            ]
