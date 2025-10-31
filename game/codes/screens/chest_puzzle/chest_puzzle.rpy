screen chest_puzzle:
    frame:
        background "#00000080"
        xfill True
        yfill True
    
    imagebutton:
        idle "chest-closed-1.png"
        hover "chest-closed-2.png"
        at chest_transform
        action [
            Hide("chest_puzzle"),  # menutup screen saat diklik
        ]

    on "show" action Function(reset_chest_puzzle)

    key ["K_SPACE", "mousedown_1"] action If(
        chest_unlocked,
        [Hide("chest_puzzle", transition=Fade(1, 1, 1))],
        Function(check_slider_safe_zone)
    )
    
    if fatimah_photo_collected == True:
        image "cock_pit_final_02.png"
        # scene cock_pit_final_02
    else:
        image "cock_pit_final_01.png"
        # scene cock_pit_final_01

    # image "background.png" at half_size

    if is_game_over:
        timer 0.1 action [Return(False)]
    
    if not chest_unlocked:
        # frame:
        #     background "#FFFFFF"
        #     padding (5, 5)
        #     align (0.5, 0.3)
        #     vbox:
        #         text "Attempts left: [chest_unlock_tries]" size 18 color "#000000" xalign 0.5
        #         text "Successes: [chest_success_count]/3" size 18 color "#000000" xalign 0.5

        frame:
            background None
            align (0.5, 0.4)
            xysize slider_bar_size
            image "slider-bar.png" at half_size
            add slider_SM
        if chest_success_count == 0:
            image "idle.png" align (0.5, 0.7) at half_size
        else:
            image "gagal.png" align (0.5, 0.7) at half_size

    else:
        image "berhasil.png" align (0.5, 0.7) at chest_unlocked_anim
        timer 5.0 action [Hide("chest_puzzle"), Return(True)]
        key ["mousedown_1", "K_SPACE"] action [Return(True), Hide("chest_puzzle")]