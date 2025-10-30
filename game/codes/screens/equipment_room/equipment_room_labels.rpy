label gear:
    Galang "Looks like a spare part for the engine."
    return

transform gear_button:
    anchor (0.5, 0.5)
    align (0.756, 0.408)
    on hover:
        zoom 0.35
        linear 0 zoom 0.36
    on idle:
        zoom 0.36
        linear 0 zoom 0.35

label pancing:
    Galang "Did the fishing line just twitch? That came out of nowhere."
    return

transform pancing_button:
    anchor (0.5, 0.5)
    align (0.816, 0.200)
    on hover:
        zoom 0.35
        linear 0 zoom 0.36
    on idle:
        zoom 0.36
        linear 0 zoom 0.35

label kunci_inggris:
    Galang "A wrench. I could probably use it later."
    return

transform kunci_inggris_button:
    anchor (0.5, 0.5)
    align (0.820, 0.483)
    on hover:
        zoom 0.33
        linear 0 zoom 0.35
    on idle:
        zoom 0.35
        linear 0 zoom 0.33

label screwdriver:
    Galang "It's a screwdriver."
    return

transform screwdriver_button:
    anchor (0.5, 0.5)
    align (0.814, 0.530)
    on hover:
        zoom 0.36
        linear 0 zoom 0.39
    on idle:
        zoom 0.39
        linear 0 zoom 0.36

label note:
    Galang "It's barely readable, the words are blurred."
    return

transform note_button:
    anchor (0.5, 0.5)
    align (0.463, 0.408)
    on hover:
        zoom 0.35
        linear 0 zoom 0.36
    on idle:
        zoom 0.36
        linear 0 zoom 0.35

label plastik_item:
    Galang "A used black plastic bag. Probably for storing bait or scraps."
    return

transform plastik_item_button:
    anchor (0.5, 0.5)
    align (0.676, 0.796)
    on hover:
        zoom 0.35
        linear 0 zoom 0.37
    on idle:
        zoom 0.37
        linear 0 zoom 0.35

label rope:
    Galang "This rope's no good, it wouldn't hold much weight."
    return

transform rope_button:
    anchor (0.5, 0.5)
    align (0.740, 0.664)
    on hover:
        zoom 0.33
        linear 0 zoom 0.34
    on idle:
        zoom 0.34
        linear 0 zoom 0.33

label terpal:
    Galang "A grimy tarp is draped over a hidden shape."
    return

transform terpal_button:
    anchor (0.5, 0.5)
    align (0.147, 0.908)
    on hover:
        zoom 0.192
        linear 0 zoom 0.194
    on idle:
        zoom 0.194
        linear 0 zoom 0.192

label toolbox:
    Galang "The tools inside are neatly arranged. I might need this for the engine."
    return

transform toolbox_button:
    anchor (0.5, 0.5)
    align (0.852, 0.642)
    on hover:
        zoom 0.348
        linear 0 zoom 0.368
    on idle:
        zoom 0.368
        linear 0 zoom 0.348

label fanbelt:
    # sfx
    play voice "Pick Up Item_sfx.mp3"
    Galang "A spare fanbelt. It looks worn, but it should hold."
    return

transform fanbelt_button:
    anchor (0.5, 0.5)
    align (0.812, 0.375)
    on hover:
        zoom 0.31
        linear 0 zoom 0.34
    on idle:
        zoom 0.34
        linear 0 zoom 0.31