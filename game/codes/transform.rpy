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

transform shake:
    linear 0.03 xoffset 5 yoffset -3
    linear 0.03 xoffset -4 yoffset 2
    linear 0.03 xoffset 3 yoffset -2
    linear 0.03 xoffset -3 yoffset 1
    repeat 5

transform slide_up(y_target=0.5, delay=0):
    yalign 1.2
    pause delay
    easein 0.8 yalign y_target

transform chest_center:
    align (0.5, 0.7)

transform glitch_effect:
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 yoffset 5
    linear 0.05 yoffset -5
    linear 0.03 alpha 0.8
    linear 0.03 alpha 1.0
    repeat 5
