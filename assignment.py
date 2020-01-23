# name = 'Chris'
# age = '12'
# favourite_colour = 'Blue'

# print('My name is '+ name +' I am '+ age +'years old and my favourite colour is '+ favourite_colour)


# day = 'Today'

# breakfast = 'oats'
# lunch = 'fruit'
# dinner = 'casserole'

# print('{} I had {} for breakfast'.format(day,breakfast))
# print('{} I had {} for lunch'.format(day,lunch))
# print('{} I had {} for dinner'.format(day,dinner))

# day = 'Tomorrow'

# breakfast = 'cornflakes'
# lunch = 'sandwich'
# dinner = 'pizza'

# print('{} I will have {} for breakfast'.format(day,breakfast))
# print('{} I will have {} for lunch'.format(day,lunch))
# print('{} I will have {} for dinner'.format(day,dinner))

from datetime import date
birth_date = date(1961, 9, 10)
current_date = date.today()
difference_days = current_date - birth_date
print(difference_days.days)





# space1 = 'X'
# space2 = 'O'
# space3 = ' '
# space4 = 'X'
# space5 = 'X'
# space6 = ' '
# space7 = 'O'
# space8 = ' '
# space9 = ' '

# print('   |   |   ')
# print(' {} | {} | {} '.format(space1,space2,space3))
# print('   |   |   ')
# print('-----------')
# print('   |   |   ')
# print(' {} | {} | {} '.format(space4,space5,space6))
# print('   |   |   ')
# print('-----------')
# print('   |   |   ')
# print(' {} | {} | {} '.format(space7,space8,space9))
# print('   |   |   ')
