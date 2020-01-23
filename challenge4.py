# Create a variable called num.
# If num is divisible by 3 print “fizz”, if it’s divisible by 5
# print “buzz”, if it’s divisible by both 3 and 5 print “fizz
# buzz”. Otherwise print num

num = 16
text = ''
if num % 3 == 0 and num % 5 == 0:
    print('fizzbuzz')
elif num % 3 == 0 :
    print('fizz')
elif num % 5 == 0:
    print('buzz')
else:
    print(num)