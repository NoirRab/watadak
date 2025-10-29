label arc_3:
    # stop bgm 1
    stop music fadeout 1.0
    # play bgm 2
    play music "Awful Things_03.ogg" loop
    
    scene tankgelem
    narrator "A hard splash erupted on the side of the boat. Mr. Mulyo was in the water. He surfaced, thrashing against the waves. He flailed, his hands scrabbled at the surface, trying to find something, anything, to hold onto."
    Galang "DAD, HANG ON!"

    scene tankgelem_bjir with vpunch
    narrator "Galang froze. His heart hammered against his ribs, his mind screaming with a panic so loud it drowned out all thought."
    Galang "Shit, shit, what do I do…?!"
    menu:
        "{b}Abandon him.{/b} Turn and flee to the safety of the deck.":
            # sfx
            play voice "Klik_sfx.mp3"
            scene digidaw
            narrator "With a final, horrified glance at the thrashing water, Galang stumbled backward."
            narrator "His survival instinct screamed louder than his conscience."
            narrator "He turned and sprinted for the cabin, slamming the door shut as if he could lock out the sight and the sound, the guilt already coiling in his gut."
            narrator "From the porthole, he watched... One moment Mr. Mulyo's hand was clawing at the air; the next, a dark wave rolled over the spot, leaving nothing but empty, churning water."
            narrator "He was gone."
        "{b}Jump in.{/b} Leap into the churning water to try and pull him out.":
            # sfx
            play voice "Klik_sfx.mp3"
            scene nyebur
            narrator "There was no time to think, he needed to act."
            narrator "Galang scrambled onto the gunwale and threw himself into the black, icy water."
            narrator "The cold knocked the air from his lungs."
            narrator "He fought through the waves, reaching the spot where Mr. Mulyo was just struggling, his own hands grasping blindly in the murk."
            $ is_ending = True
            $ ending_choice = 3
            return
        "{b}Save him.{/b} Fling the nearest life buoy or rope.":
            # sfx
            play voice "Klik_sfx.mp3"
            scene per_lampung
            narrator "\"HOLD ON!\" Galang bellowed, his voice raw."
            narrator "He scrambled for the lifebuoy hanging on the cabin wall, his fingers fumbling with the knot."
            narrator "He heaved it with all his strength, the ring landing a mere foot from Mr. Mulyo's grasping fingers."
            narrator "Mr. Mulyo made a desperate lunge for it, his fingertips brushing the rope. But a powerful undertow, as if summoned by the taboo, dragged him down and away."
            narrator "The lifebuoy floated, useless, on the empty water where he vanished."
        "{b}Stand still.{/b} Stand paralyzed and watch.":
            # sfx
            play voice "Klik_sfx.mp3"
            scene per_lampung
            narrator "Paralyzed, Galang could only watch the horror unfold."
            narrator "His feet were rooted to the spot, his mind screaming commands that his body refused to obey."
            narrator "He saw Mr. Mulyo's desperate eyes, his silent plea, before a wave, or something in the wave, crashed over him."
            narrator "When it receded, there was nothing but empty, churning water."
            narrator "The moment for action passed. The sea grew calm. Galang stood alone on the boat, the image of Mr. Mulyo's last look seared into his memory, a ghost forever haunting his inaction."
    return