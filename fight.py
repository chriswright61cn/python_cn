import random

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
