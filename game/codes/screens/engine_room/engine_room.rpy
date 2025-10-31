screen engine_room:
    imagebutton:
        idle "eng_gene_room/tenki_idle.png"
        hover "eng_gene_room/tanki.png"
        at tanki_button
        action [
            Play("voice", "audio/Gas kang_sfx.mp3"), 
            Hide("engine_room"),
            Call("tanki")
            ]
    imagebutton:
        idle "eng_gene_room/jerigen_2_idle.png"
        hover "eng_gene_room/jerigen_2.png"
        at jerigen_2_button
        action [
            Play("voice", "audio/Pick Up Item_sfx.mp3"), 
            Hide("engine_room"),
            Call("jerigen_2")
            ]
    imagebutton:
        idle "eng_gene_room/kunci_enggres_idle.png"
        hover "eng_gene_room/kunci_enggres.png"
        at kunci_enggres_button
        action [
            Play("voice", "audio/Metal tool_sfx.mp3"), 
            Hide("engine_room"),
            Call("kunci_enggres")
            ]
    imagebutton:
        idle "eng_gene_room/toolbox_2_idle.png"
        hover "eng_gene_room/toolbox_2.png"
        at toolbox_2_button
        action [
            Play("voice", "audio/Toolbox_sfx.mp3"), 
            Hide("engine_room"),
            Call("toolbox_2")
            ]
    imagebutton:
        idle "eng_gene_room/pasang_fanbelt_idle.png"
        hover "eng_gene_room/pasang_fanbelt.png"
        at pasang_fanbelt_button
        action [
            Play("voice", "audio/Fanbelt_sfx.mp3"), 
            Hide("engine_room"),
            Call("pasang_fanbelt")
            ]