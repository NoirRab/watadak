label arc_1_choices_1_result:
    scene arc1_05
    Mulyo "Look, son, rumors could be true, but they usually aren't. Forget the stories."
    scene arc1_06
    Mulyo "What's real is that Fatimah is suffering. We are here for her. Let that be your focus."
    scene arc1_01 with Fade (1.0, 0.0, 1.0)
    pause 1.0
    narrator "."
    pause 0.3
    narrator ". ."
    pause 0.3
    narrator ". . ."
    pause 0.3
    scene arc1_06
    Mulyo "Galang, fetch me my cigarettes, would you?"
    #skrip rokok
    scene cock_pit_01 with fade
    stop sound fadeout 1.0
    play sound "Ship Interior Ambi_04.mp3" 
    call screen cockpit_01