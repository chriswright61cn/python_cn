# import game_data
scene_data = {
    "scene1": {
        "option1_text":"this is option 1",
        'option1_action':"fight"
        },
    "scene2": {
        "option1_text":"this is option 1",
        'option1_action':"load_scene",
        'scene_name':'scene3'
        },
    "scene3": {
        "option1_text":"this is option 1",
        'option1_action':"fight"
        },
    "scene4": {
        "option1_text":"this is option 1",
        'option1_action':"load_scene"
        }
}

# current_scene = scene_data['scene1']
# print(current_scene)
# print(current_scene['option1_action'])

# def load_scene(scene_name):
#     scene_data[scene_name]['option1_action']

# load_scene('scene2')