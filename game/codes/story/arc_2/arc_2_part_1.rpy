label arc_2_part_1:
    Galang "Right. Better get this to him."
    scene arc1_07 with fade
    stop sound
    play sound "Oceanatnight_01.mp3"
    Galang "Here, your cigarettes."
    Galang "{i}He's right. She needs me. So what if it's taboo? I will bear any suffering if it spares her hers. The red moon doesn't frighten me... but the thought of watching Fatimah in pain, powerless to stop it, terrifies me.{i}"
    scene pembuka_arc2 with Fade (0.5, 0.0, 0.5)
    pause 1.6
    scene arc2_02 with Fade (0.5, 0.0, 0.5)
    pause 1.6
    scene arc2_03 with Fade (0.5, 0.0, 0.5)
    pause 1.6
    scene bulan with Fade (0.5, 0.0, 0.5)
    menu:
        "Dad… The Moon… It's…":
            jump arc_2_choices_1_a
        "Are you sure the rumors aren't true?":
            jump arc_2_choices_1_b
        "... Dad, I think the moon's color is changing.":
            jump arc_2_choices_1_c