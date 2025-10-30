label arc_1:
    scene black
    # play bgm 1
    play music "HorrorAmbience_01.mp3" loop
    
    Galang "This is for her. It's all for Fatimah."
    narrator "I hammered that thought into my head, a mantra to ward off my fear." 
    narrator "Just before I killed the engine of this old car, my hand brushed against something cold next to the steering wheel: a voice recorder, a gift from the office for 'jotting down hot property ideas anywhere."
    narrator "I slipped it into my pocket."
    narrator "Who knows… Maybe out in the middle of the ocean, a brilliant idea for selling the only piece of land Fatimah inherited would come to me."
    narrator "Or perhaps, it was just to record my own voice, so I wouldn't feel so alone in the darkness we were about to cross."
    narrator "Through the car window, the pitch-black sea was already waiting. The silhouette of Mr. Mulyo, my father-in-law, stood on the pier like a statue that had grown there for centuries."
    narrator "I took a deep breath, trying to calm my restless soul."
    
    scene 1000 with fade  
    narrator "The smell of the hospital's disinfectant seemed to cling to me, mixed with the memory of Fatimah's pale face from this afternoon."
    narrator "She forced a smile, saying, 'Be careful, dear.'"
    
    scene 1 with fade
    # play audio 1
    play sound "Oceanatnight_01.mp3" loop
    
    narrator "The only light came from the full moon hanging in the sky, glinting on the water's gently rippling surface."
    narrator "The sea wind stabbed through me, carrying the scent of salt and fish, and the wooden boat voiced its dissent in a soft, uneasy creak."
    narrator"At the stern, Mr. Mulyo sat with his weathered body, his face etched with deep wrinkles. His hands were busy checking the rolls of the fishing line, his movements the pure reflex of an old fisherman."
    narrator "I could only sit restlessly beside him; my shirt damp, my breath short, my eyes darting back and forth between the full moon above and the ever-darkening sea below."
    
    scene arc1_01 with Fade (0.6, 0.0, 0.6)
    pause 1.0
    
    scene arc1_02
    Galang "Dad... About the stories... the ones where fishermen are forbidden to go to sea on a full moon... Is it—"
    
    scene arc1_03
    Mulyo "They called it a taboo. The red moon will appear, they said. Its bloody light would awaken the sea to devour anyone who dares disturb its slumber."
    
    scene arc1_07
    
    menu:
        "Devour…? I don't understand…":
            # sfx
            play voice "Klik_sfx.mp3"

            scene arc1_04
            Galang "Devour…? I don't understand…"
            
            scene arc1_03
            
            Mulyo "Oh, people had their theories; Some said fishermen were pulled down by the waves, or taken by things in the deep. But I never bought it. Just a tall tale to keep folks off the water, especially on a night like this when the fishing's good."
            scene arc1_07

            menu:
                "So, you don't believe the rumors?":
                    # sfx
                    play voice "Klik_sfx.mp3"
                    scene arc1_04
                    Galang "So, you don't believe the rumors?"
                "Yeah, I guess you're right...":
                    # sfx
                    play voice "Klik_sfx.mp3"
                    scene arc1_04
                    Galang "Yeah, I guess you're right..."
            
            scene arc1_05
            Mulyo "Look, son, rumors could be true, but they usually aren't. Forget the stories."
            
            scene arc1_06
            Mulyo "What's real is that Fatimah is suffering. We are here for her. Let that be your focus."
            
            scene arc1_01 with Fade (1.0, 0.0, 1.0)
            narrator "."
            pause 0.3
            narrator ".."
            pause 0.3
            narrator "..."
            pause 0.3
            
            scene arc1_06
            Mulyo "Galang, fetch me my cigarettes, would you?"
            
            scene cock_pit_01 with fade
            # stop audio 1
            stop sound fadeout 1.0
            # play audio 2
            play sound "Ship Interior Ambi_04.mp3" loop
            
            call screen cockpit

            return
