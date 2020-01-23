import random

character_data = {
"name": "Bob",
"base_health": 30,
"base_attack": 30,
"base_defence": 30,
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
"current_health": 30,
"current_attack": 30,
"current_defence": 30
}

scene_1 = {
"scene_title":"Prison Cell",
"scene_description": "You awaken in a dark cell, head throbbing and body aching from the battle earlier that day. \n You hear soft footsteps outside, a short silence before a click as the lock is turned. The door opens to reveal your mother, the queen in a dark robe. She stealthily moves towards you and whispers, Bob Thank god you are OK! Come with me quickly, we don't have much time.",
"option_1_text": "Immediately exit the cell with her",
"option_1_function": "Load_scene",
"option_1_function_text": "scene_2",
"option_1_display": True,
"option_2_text": "Ask, 'We lost? Is Jennifer safe?",
"option_2_function": "display-message",
"option_2_function_text": "We did... I'm sorry Bob... That tyrant, Archibald took her'. Footsteps then the door flings open! Guards enter and the captain gives the orders, 'Take that slag to a cell, we\'ll have fun with her later... And slit that pricks throat!",
"option_2_display": True,
"option_3_text": "Do Nothing",
"option_3_function": "",
"option_3_display": True,
"option_4_text": "should not display",
"option_4_function": "",
"option_4_display": False,
"enemy_exists": False,
"enemy_alive": False,
"enemy_name": "ogre",
"enemy_health": 5,
"enemy_attack": 5,
"enemy_defence": 5,
"chest_exists": "",
"chest_contents_name": "",
"chest_full": "",
"riddle_text": "",
"riddle_answer": "",
"success": "",
"success_text": "",
"success_function_name": "" }

scene_2 = {
"scene_description": "scene 2 description",
"option_1_text": "Go to scene 1",
"option_1_function": "Load_scene",
"option_1_scene_load": "scene_1",
"option_1_display": "True",
"option_2_text": "",
"option_2_function": "",
"option_2_display": "",
"option_3_text": "",
"option_3_function": "",
"option_3_display": "False",
"option_4_text": "",
"option_4_function": "",
"option_4_display": "False",
"enemy_exists": "",
"enemy_alive": "",
"enemy_name": "",
"enemy_health": "",
"enemy_attack": "",
"enemy =_defence": "",
"chest_exists": "",
"chest_contents_name": "",
"chest_full": "",
"riddle_text": "",
"riddle_answer": "",
"success": "",
"success_text": "",
"success_function_name": "" }

def option_display():
    print('Your Options are')
    option_string = ''
    if current_scene["option_1_display"]:
        print ('a: ' + current_scene["option_1_text"])
        option_string +='a'
    if current_scene["option_2_display"]:
        print ('b: '+ current_scene["option_2_text"])
        option_string +='b'
    if current_scene["option_3_display"]:
        print ('c: '+ current_scene["option_3_text"])
        option_string +='c'
    if current_scene["option_4_display"]:
        print ('d: '+ current_scene["option_4_text"])
        option_string +='d'
    option_chosen = False
    while option_chosen != True:
        option_choice = input('Choose an option:')
        if option_choice.lower() in option_string:
            print('valid choice')
            option_chosen = True
            return option_choice.lower()
        else:
            print('try again')
            
            def scene_display (scene):
    print(scene['scene_description'])
    
    # print(scene_1['enemy_attack'])# user_input = input("Your Answer?")
# print(user_input)

    def calc_damage(attack, defence):

    return (attack + random.randint(1,10) - defence)
    
    def calc_opponent_health (health, attack, defence):
    return (health - calc_damage(attack, defence))
    
    def calc_hero_health (health, attack, defence):
    return (health - calc_damage(attack, defence))
    
    def fight(hero_health, hero_attack, hero_defence, opponent_health, opponent_attack, opponent_defence ):
    both_alive = True
    while both_alive:
        new_opponent_health = calc_opponent_health(opponent_health,hero_attack,opponent_defence)
        if new_opponent_health <= 0:
            print('enemy defeated')
            both_alive = False
        else:
            print(new_opponent_health)
            opponent_health = new_opponent_health
            
        new_hero_health = calc_hero_health(hero_health, opponent_attack, hero_defence)
        if new_hero_health <= 0:
            print('You are dead')
            both_alive = False
        else:
            print('health  ')
            print(new_hero_health)
            hero_health = new_hero_healthdef load_scene(scene_name):
            
    current_scene = scene_name
    
# print(current_scene["option_2_display"])# current_scene["enemy_health"]
# current_scene["enemy_attack"]
# current_scene["enemy_defence"]
# character_data["current_health"]
# character_data["current_attack"]
# character_data["current_defence"]current_scene = scene_1
scene_display(current_scene)
# print(option_display())
# print(current_scene['option_1_function'])
# print(current_scene['option_1_function_text'])# current_scene = scene_2
load_scene(scene_2)# load_scene(current_scene['option_1_function_text'])
scene_display(current_scene)
# print(option_display())# print(current_scene[option_1_function_text])# "": "Load_scene",
# "option_1_scene_load": "scene_2",
# option_function# fight(character_data["current_health"], character_data["current_attack"], character_data["current_defence"], current_scene["enemy_health"],current_scene["enemy_attack"], current_scene["enemy_defence"])