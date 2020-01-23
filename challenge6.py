
# Create a variable called num.
# Check if the number is a palindrome (looks the same
# forward as it does backwards e.g. 1001 or 20202)

num = 1233321
num_string = str(num)
num_string_reversed = num_string[::-1]
if num_string == num_string_reversed:
    print('{} is a Palindrome'.format(num_string))
else:
    print('{} is a Not a Palindrome'.format(num_string))
