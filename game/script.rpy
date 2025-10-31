label start:
    call arc_1 from _call_arc_1
    call arc_2 from _call_arc_2
    call arc_3 from _call_arc_3
    if ending_choice is None:
        call arc_4 from _call_arc_4
    if ending_choice is None:
        call arc_5 from _call_arc_5

    # if is_game_over:
    #     return
    call show_ending from _call_show_ending
    return