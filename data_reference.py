character_data = {
    "current_scene": "scene_1",
    "name": "Bob",
    "dead": False,
    "base_health": 20,
    "base_attack": 20,
    "base_defence": 20,
    "has_ring": False,
    "ring_health": 1,
    "has_necklace": False,
    "necklace_health": 0,
    "has_shield": False,
    "shield_health": 0,
    "has_sword1": False,
    "sword_1_attack": 0,
    "has_sword2": False,
    "sword_2_attack": 0,
    "has_sword3": False,
    "sword_3_attack": 0,
    "max_sword_attack": 0,
    "has_key": False,
    "current_health": 20,
    "current_attack": 20,
    "current_defence": 20
}

scene_1 = {
    "scene_title":"Prison Cell",
    "scene_description": "You awaken in a dark cell, head throbbing and body aching from the battle earlier that day. \n You hear soft footsteps outside, a short silence before a click as the lock is turned. The door opens to reveal your mother, the queen in a dark robe. She stealthily moves towards you and whispers, Bob Thank god you are OK! Come with me quickly, we don't have much time.",
    "option_1_text": "Immediately exit the cell with her",
    "option_1_outcome_text": "You leave the cell with your mother",
    "option_1_display": True,
    "option_2_text": "Ask, 'We lost? Is Jennifer safe?",
    "option_2_outcome_text": "We did... I'm sorry Bob... That tyrant, Archibald took her'. Footsteps then the door flings open! Guards enter and the captain gives the orders, 'Take that slag to a cell, we\'ll have fun with her later... And slit that pricks throat!",
    "option_2_display": True,
    "option_3_text": "Do Nothing",
    "option_3_outcome_text":"Not so clever... The guards come in and run you and your mother through with swords. You definitely deserved that...",
    "option_3_display": True,
    "option_4_text": "",
    "option_4_outcome_text": "",
    "option_4_display": False,
}

scene_2 = {
    "scene_title":"The Tunnel",
    "scene_description": "Your mother, Queen Xenia, leads you quietly to a secret passage in the basement of the castle. You pass through and come across 2 dead guards at the feet of Queen Xenia's bodyguard. Their weapons lay loose in their death grip: \n Do you:",
    "option_1_text": "Exclaim loudly, 'Godwin, you old rascal. You could have left some for me?'",
    "option_1_display": True,
    "option_1_outcome_text": "Your excessively loud greeting results in an army of guards being alerted. You put up a decent fight but they outnumber you 10 - 1. You watch as your mother and friend are cut to pieces and then you lose your head...",
    "option_2_text": "Quickly take a sword and head along the forest path to the cross-roads",
    "option_2_display": True,
    "option_2_outcome_text": "You reach down and take one of the guard's sword then move - it's standard issue but it is well balanced and feels good in your hand. (att increased by 2).",
    "option_3_text": "Head along the forest path immediately",
    "option_3_display": True,
    "option_3_outcome_text": "You flee down the forest path with your mother and Godric close by",
    "option_4_text": "Take armour and sword from the dead men",
    "option_4_display": True,
    "option_4_outcome_text": "You start to remove a dead guards armour... Just as you pull it over your head, 2 guards come through the passage. Unarmed and outnumbered, your life flashes before your eyes as your head is cleaved from your neck.",
    }
scene_3 = {
    "scene_title":"Forest Path",
    "scene_description": "As you travel further in to the woods, your mother asks you to halt. 'Bob, I strongly advise we stop at the inn to speak to the bar keep. He is a valuable source of information and can help you understand the adventure that awaits you.'",
    "option_1_text": "Ignore your mother and head straight to the cross-roads (don't receive game overview)",
    "option_1_display": True,
    "option_1_outcome_text": "You rush towards the crossroads",
    "option_2_text": "Go to the inn with your mother (receive game overview)",
    "option_2_display": True,
    "option_2_outcome_text": "'You're right, mother, a helping hand is always welcome",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }
scene_4 = {
    "scene_title":"The Inn",
    "scene_description": "You enter the inn. Amazingly, despite recent events, it appears completely in tact with the inn keep entertaining customers. The inn keep spies you, shepherds you in to a quiet side room and gives you the following information: \n \n 'You must travel to Archibald's Castle in the deep south, to avenge your father and rescue your princess.' \n \n 'I'm not certain that you are strong enough right now and you are ill equipped.' \n \n 'You're direct route to Archibald is South but I would encourage you to consider paths to the west or east as well to speak to your allies and gain some equipment and experience along the way.'",
    "option_1_text": "",
    "option_1_display": False,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": False,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }
scene_5 = {
    "scene_title":"ambush_Cross-roads",
    "scene_description": "A small band of guards ambush you as you reach the Cross-Roads. You face your first test in battle. Godric and the Queen act fast and you follow them into the fray:",
    "option_1_text": "",
    "option_1_display": False,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": False,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    "enemy_health": 15,
    "enemy_attack": 15,
    "enemy_defence": 15,
    }
scene_6 = {
    "scene_title":"Home Crossroads",
    "scene_description": "'Well fought Bob, we must move quickly! Will you...:",
    "option_1_text": "...head back to the inn to have a few pints before you head on your way?",
    "option_1_display": True,
    "option_1_outcome_text": "What a ridiculous notion! Your Alcoholism has cost you more than ever; Before you make it back to the inn, you are attacked by an army of guards and they enjoy giving you an agonisingly slow death.",
    "option_2_text": "...travel west with us for a little while to help keep us safe?",
    "option_2_display": True,
    "option_2_outcome_text": "You head West in the hope of keeping your mother safe",
    "option_3_text": "...Head East to the Mountains, to seek help from wise friends",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "or head south in quick pursuit of your vengeance?",
    "option_4_display": True,
    "option_4_outcome_text": "In your haste to find head South, you find yourself on the edge of a dark forest",
    }

    # scene 7 mountains here

scene_8 = {
    "scene_title":"Forest",
    "scene_description": "The dense dark forest looms all around you. You continue cautiously, sticking to the overgrown path. n/ n/The forest is so dense to the East and West that it makes South your only option. \n \nOut of the silence comes a 'Hoooooowwwwl'! It's followed by many more... \n You guess a pack of Wolves or worse has picked up your scent.",
    "option_1_text": "Head North and face the multiple beasts?",
    "option_1_display": True,
    "option_1_outcome_text": "You were right, they had your scent and it doesn't take long until you are surrounded on all sides. \n \nYou barely have a chance to realise as a dozen Wargs spring at you and enjoy an evening snack...",
    "option_2_text": "Rush South and get out of this hostile environment as quickly as possible",
    "option_2_display": True,
    "option_2_outcome_text": "You head West in the hope of keeping your mother safe",
    "option_3_text": "...Head East to the Mountains, to seek help from wise friends",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }
a - outcome death.
b - outcome crossroads

# scene 9 barrow here

# scene 10 ?? 


scene_11 = {
    "scene_title":"Crossroads2",
    "scene_description": "You arrive at another crossroads! \n \n The signposts read: \n \n North: Forest - Enter at your peril! \n \n South: The dark castle",
    "option_1_text": "Head North into the forest...",
    "option_1_display": True,
    "option_1_outcome_text": "It's a challenge to make your way into the forest let alone through it. You make it 50 metres in... n\ n\ You hear multiple snarls... Before you can do anything to protect yourself, you feel powerful jaws around your calf... \n \n It's the first of many as a dozen Wargs leap from cover and overwhelm you! Nom Nom...",
    "option_2_text": "Head South and face your destiny!",
    "option_2_display": True,
    "option_2_outcome_text": "You travel south to face Archibald...",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }
a - outcome death
b - Tower keep.