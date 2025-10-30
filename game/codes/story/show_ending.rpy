label show_ending:
    if ending_choice is None:
        jump show_game_over 
    elif ending_choice == 3:
        # stop bgm 2
        stop music
        # play bgm ending
        play music "Strange-Zone_Looping.ogg" loop
        # stop bgm audio 3
        stop sound
        # play audio ending
        play sound "Drowning_ed3.ogg"

        scene tankgelem_beneran
        narrator "Something brushed his leg… "
        narrator "It felt like a tangle of line." 
        narrator "Before he could even scream, an immense force pulls him under."
        show tankgelem_beneran at shake
        narrator "The world dissolves into bubbles and darkness."
        narrator "On the surface, the water grows still, as if it had never been disturbed at all."
