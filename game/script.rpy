label start:
    call arc_1
    call arc_2
    call arc_3
    if not is_ending:
        call arc_4
    if not is_ending:
        call arc_5
    call show_ending
    return