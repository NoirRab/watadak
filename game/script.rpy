


define Galang = Character("Galang", color="#198c19")
define narrator = Character(color="#198c19",what_italic=True)
define Mulyo = Character ("Mr.Mulyo", color="#548184")
default player_checked_fatimah_photo = False #buat cockpit di arc 5

    

init python:
    def slider_update(st):
        # SpriteManager update function. Runs when the SpriteManager needs to update.
        # We use this to move the slider from side to side.
        global slider_speed

        for sprite in slider_sprites:
            if sprite.type == "slider":
                if round(sprite.x) < slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.x += slider_speed * chest_difficulty
                    slider_speed += 0.04
                elif round(sprite.x) >= slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.direction = "left"
                    slider_speed = 2
                elif round(sprite.x) > 0 and sprite.direction == "left":
                    sprite.x -= slider_speed * chest_difficulty
                    slider_speed += 0.04
                elif round(sprite.x) == 0 and sprite.direction == "left":
                    sprite.direction = "right"
                    slider_speed = 2
        if not stop_slider:
            return 0
        else:
            return None

    def check_slider_safe_zone():
        # Function to check if the user has successfully gotten the timing correct.
        global chest_unlocked
        global chest_unlock_tries
        global stop_slider
        global chest_success_count # MODIFICATION: nambah global variable buat success count
 
        for slider in slider_sprites:
            if slider.type == "slider":
                for safe_zone in slider_sprites:
                    if safe_zone.type == "safe-zone":
                        if safe_zone.x < slider.x < safe_zone.x + safe_zone_size[0]:
                            # MODIFICATION: ane ubah biar bisa multiple successes.
                            chest_success_count += 1
 
                            if chest_success_count >= 2:
                                # Slider is overlapping the safe-zone for the second time. The user has successfully opened the chest.
                                chest_unlocked = True
                                stop_slider = True
                                renpy.play("audio/engine-sound-effect.mp3", "sound")
                            else:
                                # First successful hit. Relocate the safe zone.
                                # You might want to play an intermediate success sound here.
                                renpy.play("audio/succes-one.mp3", "sound")
                                random_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
                                safe_zone.x = random_x
 
                        elif chest_unlock_tries > 0:
                            # Slider missed the safe-zone. We remove 1 from their attempts.
                            renpy.play("audio/error.ogg", "sound")
                            chest_unlock_tries -= 1
                            
                            # --- MODIFIKASI BARU DITAMBAHKAN DI SINI ---
                            # Pindahkan safe zone ke lokasi acak setelah gagal
                            random_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
                            safe_zone.x = random_x
                            # --- MODIFIKASI SELESAI ---
                        
                        if chest_unlock_tries == 0 and not chest_unlocked:
                            # User used up all their attempts and failed. We show them the game_over screen.
                            #Action Jump (Ending 1 atau 2)
                            renpy.show_screen("game_over")
                            stop_slider = True

    def reset_chest_puzzle():
        # Function to reset the mini-game so it can be played again.
        global chest_unlocked
        global chest_unlock_tries
        global stop_slider
        global slider_speed
        global chest_success_count # MODIFICATION: nambah global variable buat success count

        chest_unlocked = False
        chest_unlock_tries = 3
        stop_slider = False
        slider_speed = 2
        chest_success_count = 0 # MODIFICATION: ngereset success count ke 0

        for sprite in slider_sprites:
            if sprite.type == "slider":
                sprite.x = 0
            elif sprite.type == "safe-zone":
                random_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
                sprite.x = random_x

        slider_SM.redraw(0)
        renpy.restart_interaction()

transform half_size:
    zoom 0.5

transform chest_transform:
    zoom 0.5
    anchor (0.5, 0.5)
    align (0.5, 0.7)
    subpixel True
    on hover:
        easein 1.0 zoom 0.51
    on idle:
        easein 1.0 zoom 0.5

transform chest_unlocked_anim:
    zoom 0.5
    alpha 0.0
    parallel:
        easein 3.0 zoom 0.7
    parallel:
        easein 2.0 alpha 1.0

screen game_over:
    modal True
    key "K_SPACE" action [Function(reset_chest_puzzle), Hide("game_over")]
    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            background "#FFFFFFE6"
            xfill True
            padding (15, 0)
            align (0.5, 0.5)
            text "Game Over!" color "#000000" size 34 xalign 0.5

screen chest_puzzle:
    on "show" action Function(reset_chest_puzzle)
    key ["K_SPACE", "mousedown_1"] action If(chest_unlocked, true = [Hide("chest_puzzle", transition = Fade(1, 1, 1)), Show("scene_1")], false = Function(check_slider_safe_zone))
    image "background.png" at half_size
    if not chest_unlocked:
        frame:
            background "#FFFFFF"
            padding (5, 5)
            align (0.5, 0.3)
            # MODIFICATION: nambah  vbox buat display attempts dan successes.
            vbox:
                text "Attempts left: [chest_unlock_tries]" size 18 color "#000000" xalign 0.5
                text "Successes: [chest_success_count]/2" size 18 color "#000000" xalign 0.5

        frame:
            background None
            align (0.5, 0.4)
            xysize slider_bar_size
            image "slider-bar.png" at half_size
            add slider_SM
        if chest_success_count == 0:
            image "idle.png" align (0.5, 0.7) at half_size
        else: # Ini berarti chest_success_count adalah 1
            image "gagal.png" align (0.5, 0.7) at half_size
        # --- MODIFIKASI SELESAI ---

    else:
        image "berhasil.png" align (0.5, 0.7) at chest_unlocked_anim

screen scene_1:
    image "background.png" at half_size
    imagebutton auto "chest-closed-%s.png" action [Hide("scene_1"), Show("chest_puzzle")] at chest_transform

screen cockpit01: #hover rokok
    imagebutton:
        idle "rock_cock.png"
        hover "rock_cock_hover.png"
        xanchor -253
        yanchor -15
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Pick Up Item_sfx.mp3"), Jump("arc2")
    imagebutton:
        idle "fud_can_idle.png"
        hover "fud_can.png"
        xanchor 651
        yanchor -120
        xpos 0.5
        ypos 0.28
        action Jump("kaleng")
    imagebutton:
        idle "wall_et_idle.png"
        hover "wall_et.png"
        xanchor 480
        yanchor -210
        xpos 0.5
        ypos 0.28
        action Jump("Dompet")
    imagebutton:
        idle "buck_trush_idle.png"
        hover "buck_trush.png"
        xanchor 254
        yanchor -260
        xpos 0.5
        ypos 0.28
        action Jump("Plastik")
    imagebutton:
        idle "notde1_idle.png"
        hover "notde1.png"
        xanchor -395
        yanchor 156
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Paper_sfx.wav"), Jump("Note1")
    imagebutton:
        idle "radio_idle.png"
        hover "radio.png"
        xanchor -67
        yanchor 224
        xpos 0.5
        ypos 0.28
        action Jump("Radio")
    imagebutton:
        idle "notde2_idle.png"
        hover "notde2.png"
        xanchor 275
        yanchor 146
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Paper_sfx.wav"), Jump("Note2")
    imagebutton:
        idle "keluar_ga_pict_01_idle.png"
        hover "keluar_ga_pict_01.png"
        xanchor 170
        yanchor 112
        xpos 0.5
        ypos 0.28
        action [SetVariable("player_checked_fatimah_photo", True), Play("sound", "audio/Pick Up Item_sfx.mp3"), Jump("fotofatimaharc2")]
screen cockpit02:
    imagebutton:
        idle "rock_cock.png"
        hover "rock_cock_hover.png"
        xanchor -253
        yanchor -15
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Pick Up Item_sfx.mp3"),Jump("arc2")
    imagebutton:
        idle "fud_can_idle.png"
        hover "fud_can.png"
        xanchor 651
        yanchor -120
        xpos 0.5
        ypos 0.28
        action Jump("kalengF")
    imagebutton:
        idle "radio_idle.png"
        hover "radio.png"
        xanchor -67
        yanchor 224
        xpos 0.5
        ypos 0.28
        action Jump("RadioF")
    imagebutton:
        idle "wall_et_idle.png"
        hover "wall_et.png"
        xanchor 480
        yanchor -210
        xpos 0.5
        ypos 0.28
        action Jump("DompetF")
    imagebutton:
        idle "buck_trush_idle.png"
        hover "buck_trush.png"
        xanchor 254
        yanchor -260
        xpos 0.5
        ypos 0.28
        action Jump("PlastikF")
    imagebutton:
        idle "notde1_idle.png"
        hover "notde1.png"
        xanchor -395
        yanchor 156
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Paper_sfx.wav"), Jump("Note1F")
    imagebutton:
        idle "notde2_idle.png"
        hover "notde2.png"
        xanchor 275
        yanchor 146
        xpos 0.5
        ypos 0.28
        action Play("sound", "audio/Paper_sfx.wav"), Jump("Note2")
       
label start:
    scene black
    play music "HorrorAmbience_01.mp3"
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
    #scene bg with fade fatimah_hospital
    narrator "She forced a smile, saying, 'Be careful, dear.'"
    scene 1 with fade
    play sound "Oceanatnight_01.mp3"
    narrator "And now, in the boat, the night sea felt even darker, even heavier."
    #scene bg with fade bulan
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
            jump choices1_a
label choices1_a:
    scene arc1_04
    Galang "Devour…? I don't understand…"
    scene arc1_03
    Mulyo "Oh, people had their theories; Some said fishermen were pulled down by the waves, or taken by things in the deep. But I never bought it. Just a tall tale to keep folks off the water, especially on a night like this when the fishing's good."
    scene arc1_07
    menu:
        "So, you don't believe the rumors?":
            jump choices1_b
        "Yeah, I guess you're right...":
            jump choices1_c

label choices1_b:
    scene arc1_04
    Galang "So, you don't believe the rumors?"
    jump choices1B_common

label choices1_c:
    scene arc1_04
    Galang "Yeah, I guess you're right..."
    jump choices1B_common

label choices1B_common:
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
    call screen cockpit01
label fotofatimaharc2:
    scene cock_pit_01
    show fat_imah:
        yalign 0.5
        xalign 0.5
    Galang "I was supposed to protect her. But now... I'm out here fishing for her life while she fights for it in that hospital room."
   
    jump rokokkdoang
label rokokkdoang:
    scene cock_pit_02
    call screen cockpit02

label kaleng:
    Galang "He didn't even finish his meal. The fish can't wait, I suppose."
    call screen cockpit01

label Dompet:
    Galang "I'm not here for his wallet."
    call screen cockpit01 

label Radio:
    Galang "The radio's been dead for a while now. No use even trying it."
    call screen cockpit01

label Plastik:
    Galang "What's a plastic bag doing there?"
    call screen cockpit01

label Note1:
    Galang "... The hospital is asking for more. We need 5 million Rupiah by the end of the week or they will stop the treatment..."
    call screen cockpit01

label Note2:
    Galang "... Settlement for Fatimah binti Mulyo's treatment is overdue. A final extension is granted until Sunday, 15-09-20xx. After this date, services will be suspended..."
    call screen cockpit01

label kalengF:
    Galang "He didn't even finish his meal. The fish can't wait, I suppose."
    call screen cockpit02

label DompetF:
    Galang "I'm not here for his wallet."
    call screen cockpit02 

label RadioF:
    Galang "The radio's been dead for a while now. No use even trying it."
    call screen cockpit02

label PlastikF:
    Galang "What's a plastic bag doing there?"
    call screen cockpit02

label Note1F:
    Galang "... The hospital is asking for more. We need 5 million Rupiah by the end of the week or they will stop the treatment..."
    call screen cockpit02

label Note2F:
    Galang "... Settlement for Fatimah binti Mulyo's treatment is overdue. A final extension is granted until Sunday, 15-09-20xx. After this date, services will be suspended..."
    call screen cockpit02

label arc2:
    Galang "Right. Better get this to him."
    scene arc1_07 with fade
    stop sound
    play sound "Oceanatnight_01.mp3"
    Galang "Here, your cigarettes."
    Galang "{i}He's right. She needs me. So what if it's taboo? I will bear any suffering if it spares her hers. The red moon doesn't frighten me... but the thought of watching Fatimah in pain, powerless to stop it, terrifies me.{i}"
    scene pembuka_arc2 with Fade (2.0, 0.0, 2.0)
    pause 1.0
    scene arc2_02 with Fade (2.0, 0.0, 2.0)
    pause 1.0
    scene arc2_03 with Fade (2.0, 0.0, 2.0)
    pause 1.0
    scene bulan with Fade (2.0, 0.0, 2.0)
    menu:
        "Dad… The Moon… It's…":
            jump choices_common1a
        "Are you sure the rumors aren't true?":
            jump choices_common1b
        "... Dad, I think the moon's color is changing.":
            jump choices_common1c
label choices_common1a:
    Galang "Dad… The Moon… It's…"
    jump common
label choices_common1b:
    Galang "Are you sure the rumors aren't true?"
    jump common
label choices_common1c:
    Galang "... Dad, I think the moon's color is changing."
    jump common

label common:
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
    play sound "Brak_Sfx.mp3"
    Mulyo "CRAP-!"
    scene cing_pancing
    narrator "Galang jolted at the sound. He spun just in time to see Mr. Mulyo thrown off balance, his wrists snarled in a fishing line that snapped tight. An unseen force beneath the water was dragging him, pulling him relentlessly toward the railing."
    Mulyo "A little help, son! This is the one! Look at it fight! Land this, and we can turn for home right now!"
    scene cing_pancing_geterbjir with vpunch
    play sound "FishingRod_sfx"
    Mulyo "What the hell?! It's dragging me! GALANG! HELP M—"
    narrator "He planted his feet and pulled with all his strength, but his boots slid on the slick deck His old frame staggered, balance lost for a desperate second before" 
    scene byur with vpunch
    play sound "Kecebur_02.mp3"
    narrator "he crashed against the side of the boat and tumbled over with a sickening thud."
    Galang "DAD-!"











#ngecek doang buat arc 5
    menu:
        "Dad… The Moon… It's…":
            jump arc_5_example

label arc_5_example: #ngecek doang buat arc 5
    narrator "Beberapa waktu telah berlalu... Arc 5 dimulai."
    Galang "Aku kembali ke cockpit."
        #jika player klik foto pake cokcpit 2
    if player_checked_fatimah_photo == True:
        scene cock_pit_02
        Galang "(Ruangan ini... terasa berbeda.)"
    else:
        # Jika player DULU TIDAK klik foto, tetap pakai cockpit 1 (lama)
        scene cock_pit_01
        Galang "(Ruangan ini... masih sama seperti dulu.)"







    $slider_SM = SpriteManager(update = slider_update)
    $slider_sprites = []

    # Safe zone variables
    $safe_zone_image = Image("safe-zone.png")
    $safe_zone_transform = Transform(child = safe_zone_image, zoom = 0.5)
    $safe_zone_size = (int(149 / 2), int(70 / 2))
    $slider_sprites.append(slider_SM.create(safe_zone_transform))
    $slider_sprites[-1].type = "safe-zone"

    # Slider variables
    $slider_bar_size = (int(545 / 2), int(70 / 2))
    $slider_image = Image("slider.png")
    $slider_transform = Transform(child = slider_image, zoom = 0.5)
    $slider_sprites.append(slider_SM.create(slider_transform))
    $slider_sprites[-1].type = "slider"
    $slider_sprites[-1].direction = "right"
    $slider_size = (int(48 / 2), int(66 / 2))
    $slider_speed = 2
    $stop_slider = False

    # Chest variables
    $chest_unlocked = False
    $chest_unlock_tries = 3
    $chest_difficulty = 2
    $chest_success_count = 0 # MODIFICATION: Added variable to track successful hits.

    call screen scene_1
    return