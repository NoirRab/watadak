default visited_fish_hold = False
default visited_equipment_room = False

label arc_4:
    # stop bgm 2
    stop music
    # play bgm 3
    play music "Night-Stalker_Looping.ogg"
    
    scene lancar_kang with Fade (1.0, 0.0, 1.0)
    narrator "Galang scrambled to the ship's rail, his heart frantically thumping."
    narrator "Below, the sea was deceptively calm, showing no sign of the struggle."
    narrator "There was nothing. No splash, no cry, no Mr. Mulyo."
    narrator "The realization was still cold in his veins when the ship's engine gave a final, sickening rattle and went dead."
    # sfx
    play voice "EngineDown_sfx.mp3"
    Galang "Damn it, why now…?!"

    scene mesh_in
    narrator "Galang frantically checked the engine, his shuddering growing uncontrollable."
    show fanbelt at slide_up(0.4, delay=0.0)
    narrator "First, he found the fan belt's been ripped unnaturally."
    show fuel_panel at slide_up(0.6, delay=0.2)
    narrator "Then, he checked the fuel gauge and tapped the tank, hearing only a hollow, empty ring. There was nothing left."
    Galang "Okay, think. I need fuel and a fan belt. If I can manage that, I might still be able to restart the engine."

    call arc_4_decision_1

    return
        

label arc_4_decision_1:
    if not (visited_fish_hold and visited_equipment_room):
        show lancar_kang_kung
        menu:
            "Where should Galang go next?"

            "Go to the Fish Hold" if not visited_fish_hold:
                call arc_4_decision_1_fish_hold

            "Check the Equipment Room" if not visited_equipment_room:
                call arc_4_decision_1_equipment_room
        call arc_4_decision_1

    else:
        call arc_4_decision_1_finish

label arc_4_decision_1_fish_hold:
    # stop audio 3
    stop sound
    # play audio 4
    play sound "Ship Interior Ambi_04.mp3"
    scene store_age_room_01 with fade
    narrator "The damp air reeks of rust and diesel. A jumble of nets, fish boxes, and empty drums clutters the room, leaving little space to move."
    call arc_4_decision_1_fish_hold_loop
    return

label arc_4_decision_1_fish_hold_loop:
    call screen fish_hold
    if not visited_fish_hold:
        jump arc_4_decision_1_fish_hold_loop
    return


label arc_4_decision_1_equipment_room:
    $ visited_equipment_room = True
    return


label arc_4_decision_1_finish:
    scene bridge_bg
    with fade
    Galang "I've checked both places. Now I should report back..."
    return