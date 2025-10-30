label arc_5:
    narrator "Beberapa waktu telah berlalu... Arc 5 dimulai."
    Galang "Aku kembali ke cockpit."
        #jika player klik foto pake cokcpit 2
    if fatimah_photo_collected == True:
        scene cock_pit_02
        Galang "(Ruangan ini... terasa berbeda.)"
    else:
        # Jika player DULU TIDAK klik foto, tetap pakai cockpit 1 (lama)
        scene cock_pit_01
        Galang "(Ruangan ini... masih sama seperti dulu.)"

    $ slider_SM = SpriteManager(update = slider_update)
    $ slider_sprites = []

    # Safe zone variables
    $ safe_zone_image = Image("safe-zone.png")
    $ safe_zone_transform = Transform(child = safe_zone_image, zoom = 0.5)
    $ safe_zone_size = (int(149 / 2), int(70 / 2))
    $ slider_sprites.append(slider_SM.create(safe_zone_transform))
    $ slider_sprites[-1].type = "safe-zone"

    # Slider variables
    $ slider_bar_size = (int(545 / 2), int(70 / 2))
    $ slider_image = Image("slider.png")
    $ slider_transform = Transform(child = slider_image, zoom = 0.5)
    $ slider_sprites.append(slider_SM.create(slider_transform))
    $ slider_sprites[-1].type = "slider"
    $ slider_sprites[-1].direction = "right"
    $ slider_size = (int(48 / 2), int(66 / 2))
    $ slider_speed = 2
    $ stop_slider = False

    # Chest variables
    $ chest_unlocked = False
    $ chest_unlock_tries = 3
    $ chest_difficulty = 2
    $ chest_success_count = 0 # MODIFICATION: Added variable to track successful hits.

    call screen scene_01
    return