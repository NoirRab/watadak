default chest_difficulty = 2
default chest_success_count = 0
default chest_unlock_tries = 3
default chest_unlocked = False
default slider_speed = 2
default stop_slider = False

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
                            global is_game_over, game_over_reason
                            is_game_over = True
                            game_over_reason = "Failed to open the chest."
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