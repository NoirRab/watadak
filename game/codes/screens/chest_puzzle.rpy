screen chest_puzzle:
    on "show" action Function(reset_chest_puzzle)
    key ["K_SPACE", "mousedown_1"] action If(chest_unlocked, true = [Hide("chest_puzzle", transition = Fade(1, 1, 1)), Show("scene_01")], false = Function(check_slider_safe_zone))
    image "background.png" at half_size
    if not chest_unlocked:
        frame:
            background "#FFFFFF"
            padding (5, 5)
            align (0.5, 0.3)
            # MODIFICATION: nambah  vbox buat display attempts dan successes.
            vbox:
                text "Attempts left: [chest_unlock_tries]" size 18 color "#000000" xalign 0.5
                text "Successes: [chest_success_count]/2" size 18 color "#000000" xalign 0.5

        frame:
            background None
            align (0.5, 0.4)
            xysize slider_bar_size
            image "slider-bar.png" at half_size
            add slider_SM
        if chest_success_count == 0:
            image "idle.png" align (0.5, 0.7) at half_size
        else: # Ini berarti chest_success_count adalah 1
            image "gagal.png" align (0.5, 0.7) at half_size
        # --- MODIFIKASI SELESAI ---

    else:
        image "berhasil.png" align (0.5, 0.7) at chest_unlocked_anim