scene_1 = {
    "scene_title":"Prison Cell",
    "scene_description": "You awaken in a dark cell, head throbbing and body aching from the battle earlier that day. \n You hear soft footsteps outside, a short silence before a click as the lock is turned. The door opens to reveal your mother, the queen in a dark robe. She stealthily moves towards you and whispers, Bob Thank god you are OK! Come with me quickly, we don't have much time.",
    "option_1_text": "Immediately exit the cell with her",
    "option_1_function": Load_scene,
    "option_1_function_parameter": "scene_2",
    "option_1_display": True,
    "option_2_text": "Ask, 'We lost? Is Jennifer safe?",
    "option_2_function": "display-message",
    "option_2_message": "We did... I'm sorry Bob... That tyrant, Archibald took her'. Footsteps then the door flings open! Guards enter and the captain gives the orders, 'Take that slag to a cell, we\'ll have fun with her later... And slit that pricks throat!",
    "option_2_display": True
}

scene_2 = {
    "scene_title":"Scene 2",
    "scene_description": " scene 2 description",
    "option_1_text": "Goto next scene",
    "option_1_function": "Load_scene",
    "option_1_function_text": "scene_3",
    "option_1_display": True,
    "option_2_text": "some text?",
    "option_2_function": "display-message",
    "option_2_message": "We did... I'm sorry Bob... That tyrant, Archibald took her'. Footsteps then the door flings open! Guards enter and the captain gives the orders, 'Take that slag to a cell, we\'ll have fun with her later... And slit that pricks throat!",
    "option_2_display": True
}

current_scene = scene_1
print(current_scene['scene_description'])
# print(current_scene['option_1_function'])
# print(current_scene['option_1_function_parameter'])

def load_scene(scene):
    current_scene = scene
    # print(type(current_scene))
    # print(current_scene['scene_description'])

load_scene(scene_2)

print(current_scene['scene_description'])


# current_scene = scene_2
# print(current_scene['scene_description'])

# scene_name