label fish_box:
    Galang "Just a fish box."
    return

transform fish_box_button:
    anchor (0.5, 0.5)
    align (0, 0.96)
    on hover:
        zoom 0.35
        linear 0 zoom 0.36
    on idle:
        zoom 0.36
        linear 0 zoom 0.35

label tong_gong:
    Galang "It's empty."
    return

transform tong_gong_button:
    anchor (0.5, 0.5)
    align (0.583, 0.61)
    on hover:
        zoom 0.33
        linear 0 zoom 0.34
    on idle:
        zoom 0.34
        linear 0 zoom 0.33

label tong_jatoh:
    $ drum_fallen = True
    Galang "A heavy \"THUNK!\" echoed through the space as the barrel rolled aside."
    play voice "Drum_sfx.mp3"
    scene store_age_room_02 with fade
    return

transform tong_jatoh_button:
    anchor (0.5, 0.5)
    align (0.885, 0.74)
    on hover:
        zoom 0.32
        linear 0 zoom 0.33
    on idle:
        zoom 0.33
        linear 0 zoom 0.32

label net:
    Galang "A fishing net. Looks like it's seen some use."
    return

transform net_button:
    anchor (0.5, 0.5)
    align (0.052, 0.505)
    on hover:
        zoom 0.37
        linear 0 zoom 0.38
    on idle:
        zoom 0.38
        linear 0 zoom 0.37

label ikan:
    Galang "Where'd the fish fall from? The blood's dripping everywhere..."
    return

transform ikan_button:
    anchor (0.5, 0.5)
    align (0.66, 0.98)
    on hover:
        zoom 0.37
        linear 0 zoom 0.39
    on idle:
        zoom 0.39
        linear 0 zoom 0.37

label jerigen:
    $ visited_fish_hold = True
    Galang "Finally. There's the fuel canister."
    play voice "Pick Up Item_sfx.mp3"
    scene store_age_room_03 with fade
    return

transform jerigen_button:
    anchor (0.5, 0.5)
    align (0.875, 0.8)
    on hover:
        zoom 0.332
        linear 0 zoom 0.342
    on idle:
        zoom 0.342
        linear 0 zoom 0.332