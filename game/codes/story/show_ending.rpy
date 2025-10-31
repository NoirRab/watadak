label show_ending:
    # stop prev music and audio
    stop music
    stop sound

    if ending_choice is None:
        jump show_game_over 

    elif ending_choice == 1:
        # play bgm ending
        play music "Vast-Places_Looping.mp3" loop

        if fatimah_photo_collected == True:
            scene ending1_02
        else:
            scene ending1_01

        narrator "Galang sank to his knees, the adrenaline gone."
        Galang "It's over..."
        scene closingan_bagus
        narrator "His words were hollow, it was a whisper lost in the engine's hum and the vast, empty sea."

        $ ending_text = "ENDING 1: Escape Ending - A SOLITARY RETURN"
        jump show_ending_title

    elif ending_choice == 2:
        # play bgm ending
        play music "Vast-Places_Looping.mp3" loop
        
        scene panik_kau_dek
        narrator "The engine was dead. There was only silence."

        scene rec_order
        narrator "Galang reached for the recorder. The red record light glowed."
        # play sfx
        play voice "Recorder start_ed2.wav"
        Galang "I have a feeling this will be my first and last recording on this thing."
        Galang "The old man's boat is finished. Mulyo… Dad… is gone. I can't see the shore. There's no way out of here."
        Galang "If anyone finds this-"

        scene sini_mas_01 with dissolve
        narrator "A melody began. Not from the world he knew. It was a sound of liquid crystal and forgotten depths."
        narrator "And then, he saw her."
        narrator "Fatimah. She was standing on the water's surface, bathed in the red moon's glow, smiling the way she did before she got sick."
        
        scene sini_mas02 with dissolve
        narrator "She held out a hand. The song swelled from the space around her, like a beautiful, aching promise."
        Galang "Fatimah... I'm so sorry..."
        narrator "He stopped the recording. The file saved automatically with a timestamped name: Fri-02-37.wav"
        show sini_mas02 at glitch_effect
        narrator "He didn't think."
        narrator "He didn't hesitate."
        narrator "He climbed over the railing, her eyes locked on him, leading him into the dark, welcoming water."
        
        scene cor_an
        narrator "A fishing boat, reported missing days ago, has been found adrift and empty."
        narrator "The vessel was found in seaworthy condition with supplies and fuel onboard."
        narrator "The two crewmen, Mr. Mulyo and Galang, are missing."
        narrator "A recovered voice recorder contained a single file, Fri-02-37.wav, featuring a fragmented final message that cuts off into what investigators have classified as \"unidentifiable melodic interference.\""
        narrator "................"
        $ ending_text = "ENDING 2: Hallucination Ending - A MIRAGE OF PEACE"
        jump show_ending_title


    elif ending_choice == 3:
        # play bgm ending
        play music "Strange-Zone_Looping.ogg" loop
        # play audio ending
        play sound "Drowning_ed3.ogg" loop

        scene tankgelem_beneran
        narrator "Something brushed his leg… "
        narrator "It felt like a tangle of line." 
        narrator "Before he could even scream, an immense force pulls him under."
        show tankgelem_beneran at shake
        narrator "The world dissolves into bubbles and darkness."
        narrator "On the surface, the water grows still, as if it had never been disturbed at all."

        $ ending_text = "ENDING 3: Drowned Ending - INTO THE ABYSS"
        jump show_ending_title

label show_ending_title:
    stop music fadeout 2.0
    scene black with fade
    pause 0.5
    centered "[ending_text]" with dissolve
    pause 3.0
    # centered "THE END" with fade
    # pause
    return
