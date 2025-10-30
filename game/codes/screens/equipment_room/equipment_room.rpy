screen equipment_room:
    imagebutton:
        idle "gear_room/fanbelt_idle.png"
        hover "gear_room/fanbelt.png"
        at fanbelt_button
        action [
            Play("voice", "audio/Pick Up Item_sfx.mp3"), 
            Hide("equipment_room"),
            Call("fanbelt")
            ]
    imagebutton:
        idle "gear_room/gear_idle.png"
        hover "gear_room/gear.png"
        at gear_button
        action [
            Play("voice", "audio/Pick Up Item_sfx.mp3"), 
            Hide("equipment_room"),
            Call("gear")
            ]
    imagebutton:
        idle "gear_room/pancing_idle.png"
        hover "gear_room/pancing.png"
        at pancing_button
        action [
            Play("voice", "audio/Pick Up Item_sfx.mp3"), 
            Hide("equipment_room"),
            Call("pancing")
            ]
    imagebutton:
        idle "gear_room/kunci_inggris_idle.png"
        hover "gear_room/kunci_inggris.png"
        at kunci_inggris_button
        action [
            Play("voice", "audio/Metal tool_sfx.wav"), 
            Hide("equipment_room"),
            Call("kunci_inggris")
            ]
    imagebutton:
        idle "gear_room/screwdriver_idle.png"
        hover "gear_room/screwdriver.png"
        at screwdriver_button
        action [
            Play("voice", "audio/Metal tool_sfx.wav"), 
            Hide("equipment_room"),
            Call("screwdriver")
            ]
    imagebutton:
        idle "gear_room/note_idle.png"
        hover "gear_room/note.png"
        at note_button
        action [
            Play("voice", "audio/Paper_sfx.wav"), 
            Hide("equipment_room"),
            Call("note")
            ]
    imagebutton:
        idle "gear_room/plastik_item_idle.png"
        hover "gear_room/plastik_item.png"
        at plastik_item_button
        action [
            Play("voice", "audio/Pick Up Item_sfx.mp3"), 
            Hide("equipment_room"),
            Call("plastik_item")
            ]
    imagebutton:
        idle "gear_room/rope_idle.png"
        hover "gear_room/rope.png"
        at rope_button
        action [
            Play("voice", "audio/Pick Up Item_sfx.mp3"), 
            Hide("equipment_room"),
            Call("rope")
            ]
    imagebutton:
        idle "gear_room/terpal_idle.png"
        hover "gear_room/terpal.png"
        at terpal_button
        action [
            Play("voice", "audio/Pick Up Item_sfx.mp3"), 
            Hide("equipment_room"),
            Call("terpal")
            ]
    imagebutton:
        idle "gear_room/toolbox_idle.png"
        hover "gear_room/toolbox.png"
        at toolbox_button
        action [
            Play("voice", "audio/Toolbox_sfx.wav"), 
            Hide("equipment_room"),
            Call("toolbox")
            ]