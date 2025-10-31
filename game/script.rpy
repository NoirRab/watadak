label start:
    # call arc_1
    # call arc_2
    call arc_3
    if ending_choice is None:
        call arc_4
    if ending_choice is None:
        call arc_5

    if is_game_over:
        return
    call show_ending
    return