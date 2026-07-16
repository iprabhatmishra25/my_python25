'''
class Constants:
    @property
    def PI(self):
        return 3.14
const = Constants()

print(const.PI)  

const.PI = 3.15

from collections import namedtuple
constants= namedtuple ('constants', ['PI', 'GRAVITY'])
const = constants(PI =3.14, GRAVITY = 9.8)
print(const.PI)
print(const.GRAVITY)


# Our starting list with multiple duplicates of 2
numbers = [1, 2, 3, 2, 4, 2, 5]

# "Keep everything in numbers IF it is not equal to 2"
numbers = [x for x in numbers if x != 2]

print(numbers)
# Output: [1, 3, 4, 5
'''

# 1. Ask the user for input
text = input("Enter some text: ")

# 2. Use .upper() to force the output into ALL CAPS
print(text.upper())