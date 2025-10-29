screen game_over():
    modal True
    zorder 100

    frame:
        background "#000000AA"
        xfill True
        yfill True

        vbox:
            align (0.5, 0.5)
            spacing 20

            text "GAME OVER" size 48 color "#FF0000" xalign 0.5
            if game_over_reason:
                text "[game_over_reason]" color "#FFFFFF" xalign 0.5

            hbox:
                spacing 40
                align (0.5, 0.5)

                textbutton "Coba Lagi" action [
                    SetVariable("is_game_over", False),
                    Hide("game_over"),
                    Function(renpy.jump, last_checkpoint if last_checkpoint else "start")
                ]
                textbutton "Kembali ke Menu Utama" action [
                    SetVariable("is_game_over", False),
                    Hide("game_over"),
                    Jump("main_menu")
                ]
