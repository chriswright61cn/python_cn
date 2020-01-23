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

option = option_display()
if option == 'a':
   current_scene = scene_2
if option == 'b':
    display_message(current_scene[option_2_function_text])
if option == 'c':

if option == 'd':

def display_message(message):
    print(message)

