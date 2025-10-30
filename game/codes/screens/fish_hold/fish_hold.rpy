default drum_fallen = False

screen fish_hold:
    imagebutton:
        idle "store_age_room/fish_box_idle.png"
        hover "store_age_room/fish_box.png"
        at fish_box_button
        action [
            Play("voice", "audio/Klik_sfx.mp3"), 
            Hide("fish_hold"),
            Call("fish_box")
            ]
    imagebutton:
        idle "store_age_room/tong_gong_idle.png"
        hover "store_age_room/tong_gong.png"
        at tong_gong_button
        action [
            Play("voice", "audio/Klik_sfx.mp3"), 
            Hide("fish_hold"),
            Call("tong_gong")
            ]
    imagebutton:
        idle "store_age_room/net_idle.png"
        hover "store_age_room/net.png"
        at net_button
        action [
            Play("voice", "audio/Klik_sfx.mp3"), 
            Hide("fish_hold"),
            Call("net")
            ]
    if not drum_fallen:
        imagebutton:
            idle "store_age_room/tong_jatoh_idle.png"
            hover "store_age_room/tong_jatoh.png"
            at tong_jatoh_button
            action [
                SetVariable("drum_fallen", True),
                Hide("fish_hold"),
                Call("tong_jatoh")
                ]
    if drum_fallen:
        imagebutton:
            idle "store_age_room/ikan_idle.png"
            hover "store_age_room/ikan.png"
            at ikan_button
            action [
                Play("voice", "audio/Klik_sfx.mp3"), 
                Hide("fish_hold"),
                Call("ikan")
                ]
    if drum_fallen:
        imagebutton:
            idle "store_age_room/jerigen_idle.png"
            hover "store_age_room/jerigen.png"
            at jerigen_button
            action [
                Play("voice", "audio/Klik_sfx.mp3"), 
                Hide("fish_hold"),
                Call("jerigen")
                ]