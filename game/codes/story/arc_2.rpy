label arc_2:
    Galang "Right. Better get this to him."
    scene arc1_07 with fade
    # stop audio 2
    stop sound
    # play audio 3
    play sound "Oceanatnight_01.mp3" loop

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
            # sfx
            play voice "Klik_sfx.mp3"
            Galang "Dad… The Moon… It's…"
        "Are you sure the rumors aren't true?":
            # sfx
            play voice "Klik_sfx.mp3"
            Galang "Are you sure the rumors aren't true?"
        "... Dad, I think the moon's color is changing.":
            # sfx
            play voice "Klik_sfx.mp3"
            Galang "... Dad, I think the moon's color is changing."
    
    scene bulan
    
    show mulyo 1 at left:
        zoom 0.5 xalign 1 yalign 2
    Mulyo "Enough about the damn moon! The fish won't catch themselves!"
    
    show mulyo 2
    Mulyo "Focus, Galang! This is what we have to do!"
    hide mulyo 2 with dissolve
    narrator "His words offered no comfort." 
    narrator "The old taboo clung to Galang's mind, a cold certainty that they never should have come."
    narrator "The ship had sailed, and there was no turning back. He was still gazing upward when a sudden, sharp scream ripped him from his thoughts."
    
    scene bulan_geterbjir with vpunch
    # sfx
    play sound "Brak_Sfx.mp3"
    Mulyo "CRAP-!"
    # play again audio 3
    play sound "Oceanatnight_01.mp3" loop
    
    scene cing_pancing
    narrator "Galang jolted at the sound. He spun just in time to see Mr. Mulyo thrown off balance, his wrists snarled in a fishing line that snapped tight. An unseen force beneath the water was dragging him, pulling him relentlessly toward the railing."
    Mulyo "A little help, son! This is the one! Look at it fight! Land this, and we can turn for home right now!"
    
    scene cing_pancing_geterbjir with vpunch
    # sfx
    play sound "FishingRod_sfx.mp3"
    Mulyo "What the hell?! It's dragging me! GALANG! HELP M—"
    # play again audio 3
    play sound "Oceanatnight_01.mp3" loop
    narrator "He planted his feet and pulled with all his strength, but his boots slid on the slick deck His old frame staggered, balance lost for a desperate second before" 
    
    scene byur with vpunch
    # sfx
    play sound "Kecebur_02.mp3"
    narrator "he crashed against the side of the boat and tumbled over with a sickening thud."
    # play again audio 3
    play sound "Oceanatnight_01.mp3" loop
    Galang "DAD-!"

    return