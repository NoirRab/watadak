default result = None

label arc_5:
    scene eng_gene_room_02 with fade
    narrator "He installed the new parts with shaking hands. With the fuel and fan belt in place, Galang reached for the ignition."
    narrator "His fingers found nothing. A cold dread washed over him as he remembered that the key was in Mr. Mulyo's pocket. It was now at the bottom of the sea."
    narrator "Desperation took over, and he pried the panel open, fumbling to hotwire the engine."
    Galang "C'mon... Just gotta start the ship."

    if fatimah_photo_collected == True:
        scene cock_pit_final_02
    else:
        scene cock_pit_final_01

    Galang "Let's start fixing the engine"

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

    show screen chest_puzzle
    with fade

    scene background at half_size
    $ puzzle_success = renpy.call_screen("chest_puzzle")

    call check_game_over

    if not puzzle_success:
        return
    $ ending_choice = 1
    show berhasil at chest_center

    narrator "He gripped the wires, his knuckles white. A silent prayer formed on his lips as he touched the final connection, and-"
    return

label check_game_over:
    if is_game_over:
        $ result = renpy.call_screen("game_over")
        if result == "retry":
            call arc_5
        elif result == "exit":
            return
    return