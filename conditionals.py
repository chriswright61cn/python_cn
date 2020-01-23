age = 27
country = 'uk'
if (age > 17 and age < 25):
    print('I need to check your ID')
elif age > 24 and country.upper() =='UK':
    print('Yes, I can serve you')
else:
    print("You aren't old enough")