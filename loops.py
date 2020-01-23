# import random 
# for i in range(6):
#     print (random.randint(1,51))

# for i in range(9,-1,-1):
#     print(i)

film_list = [
    'First blood',
    'Seconds',
    'ghostbusters',
    'The third man',
    'The fourth protocol',
    'The fifth element',
]

film_list.extend(['The sixth sense', 'The seventh seal'])

for film in film_list:
    print(film)

# for index, film in enumerate(film_list):
#     print('Film number {} is {}'.format(index+1,film))

def film_check():
    if film_list[2].capitalize() == 'Ghostbusters':
        print('yey it\'s ghostbusters')
    else:
        print('booo, we want ghostbusters')

film_check()