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
    # play voice ?
    Galang "Damn it, why now…?!"

    scene mesh_in
    narrator "Galang frantically checked the engine, his shuddering growing uncontrollable."
    show fanbelt at slide_up(0.4, delay=0.0)
    narrator "First, he found the fan belt's been ripped unnaturally."
    show fuel_panel at slide_up(0.6, delay=0.2)
    narrator "Then, he checked the fuel gauge and tapped the tank, hearing only a hollow, empty ring. There was nothing left."
    Galang "Okay, think. I need fuel and a fan belt. If I can manage that, I might still be able to restart the engine."

    pause
        