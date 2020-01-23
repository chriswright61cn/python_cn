character_data = {
"name": "Bob",
"base_health": 30,
"base_attack": 30,
"base_defence": 30
}


scene1 = {
        "option1_text":"this is option 1",
        'option1_action':"fight"
        }
        
scene2 = {
        "option1_text":"this is option 1",
        'option1_action':"load_scene",
        'scene_name':'scene3'
        }

scene3 = {
        "option1_text":"this is option 1",
        'option1_action':"fight"
        }

scene4 = {
        "option1_text":"this is option 1",
        'option1_action':"load_scene"
        }

# current_scene = scene1
# current_scene = scene2
# print(current_scene)


def update_dictionary(dictionary_name, dictionary_key, dictionary_value):
    dictionary_name[dictionary_key] = dictionary_value

update_dictionary(character_data, 'name', 'Trevor')

print(character_data)

