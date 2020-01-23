# Create a variable called time, 
# a variable  place_of_work and 
# a variable called town_of_home

# Create an if statement that prints where someone is at
# times of the day. E.g. if the time is 0700 I’m at home, at
# 0800 I’m commuting, at 0900 I’m at work, etc.

time = 1500
place_of_work = 'the office'
town_of_home = 'hometown'

if time < 700:
    print('at home')
elif time > 800:
    print('travelling')
elif time > 900:
    print('at work')
elif time > 1700:
    print('travelling')
elif time > 1800 and time < 2300:
    print('at home')
else:
    print('sleeping')




