label jerigen_2:
    Galang "A fuel canister lies on its side, the content is dripping onto the floor. What a waste..."
    return

transform jerigen_2_button:
    anchor (0.5, 0.5)
    align (0.776, 0.892)
    on hover:
        zoom 0.342
        linear 0 zoom 0.352
    on idle:
        zoom 0.352
        linear 0 zoom 0.342

label toolbox_2:
    Galang "Brought this from the equipment room."
    return

transform toolbox_2_button:
    anchor (0.5, 0.5)
    align (0.254, 0.764)
    on hover:
        zoom 0.345
        linear 0 zoom 0.36
    on idle:
        zoom 0.36
        linear 0 zoom 0.345
        
label kunci_enggres:
    Galang "A fuel canister lies on its side, the content is dripping onto the floor. What a waste..."
    return

transform kunci_enggres_button:
    anchor (0.5, 0.5)
    align (0.267, 0.885)
    on hover:
        zoom 0.335
        linear 0 zoom 0.36
    on idle:
        zoom 0.36
        linear 0 zoom 0.335

label tanki:
    Galang "Gasoline splashed into the tank. The fuel's refilled."
    return

transform tanki_button:
    anchor (0.5, 0.5)
    align (0.710, 0.685)
    on hover:
        zoom 0.36
        linear 0 zoom 0.38
    on idle:
        zoom 0.38
        linear 0 zoom 0.36
        
label pasang_fanbelt:
    Galang "That's done. The fan belt's holding."
    $ visited_engine_room = True
    return

transform pasang_fanbelt_button:
    anchor (0.5, 0.5)
    align (0.44, 0.712)
    on hover:
        zoom 0.35
        linear 0 zoom 0.36
    on idle:
        zoom 0.36
        linear 0 zoom 0.35
