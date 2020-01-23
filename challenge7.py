# Create a variable called word that takes a string.
# Create an if statement that checks if the last letter is
# the same as the first.
# If it is return true, otherwise return false

#The index of the last character will be 
# length of the string minus one

# word = 'A string'
# first_char = word[0]
# last_char = word[len(word)-1]
# print(first_char)
# print(last_char)

# if first_char == last_char:
#    print(True)
# else:
#    print(False)

word = 'g string'
first_char = word[0]
last_char = word[-1]
print(first_char)
print(last_char)

if first_char == last_char:
   print(True)
else:
   print(False)