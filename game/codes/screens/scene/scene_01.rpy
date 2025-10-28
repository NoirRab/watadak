screen scene_01:
    image "background.png" at half_size
    imagebutton auto "chest-closed-%s.png" action [Hide("scene_01"), Show("chest_puzzle")] at chest_transform
