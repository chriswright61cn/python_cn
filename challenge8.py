# Take the string
# “jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuh
# gtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi”.
# Find the index of a last vowel in the string.

long_string = 'jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi'

last_a = long_string.rfind('a')
last_e = long_string.rfind('e')
last_i = long_string.rfind('i')
last_o = long_string.rfind('o')
last_u = long_string.rfind('u')

# max_vowel = max(last_a,last_e,last_i,last_o,last_u)
# vowel = long_string[max_vowel]

if (last_e > last_a) and (last_e > last_i) and (last_e > last_o) and (last_e > last_u):
   max_vowel = last_e
   vowel = 'e'
elif  (last_i > last_a) and (last_i > last_e) and (last_i > last_o) and (last_i > last_u):
   max_vowel = last_i
   vowel = 'i'
elif  (last_o > last_a) and (last_o > last_e) and (last_o > last_i) and (last_o > last_u):
   max_vowel = last_o
   vowel = 'o'
elif  (last_u > last_a) and (last_u > last_e) and (last_u > last_i) and (last_u > last_o):
   max_vowel = last_u
   vowel = 'u'  
else:
   max_vowel = last_a
   vowel='a'



print('{} is the last vowel at index {} in the string'.format(vowel,max_vowel))


# max_vowel = last_a
# vowel = 'A'

# if last_e > max_vowel:
#     max_vowel = last_e
#     vowel = 'E'

# if last_i > max_vowel:
#     max_vowel = last_i
#     vowel = 'I'

# if last_o > max_vowel:
#     max_vowel = last_o
#     vowel = 'O'

# if last_u > max_vowel:
#     max_vowel = last_u
#     vowel = 'U'
