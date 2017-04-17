# print('This is the beginning of Lecture 28')
# age=int(input("Please enter you age "))  # Converting string into int
# if 18 <= age <= 34:
#     print("You are a millenial")
# elif age < 18:
#     print("You are too young")
# elif 35 <= age <= 50:
#     print("You are Gen-X")
# else :
#     print("You are a baby-boomer")
#
# print('This is the end of Lecture 28')

# print()
# print('This is the beginning of Lecture 29')
# x=""
# if x:
#     print("x is true") # any non-empty value of this string will result in true
# else:
#     print("x is false") # if a string is empty then it is false
# y=0
# if y :
#     print('y is true')  # any non-zero value of this int will result in true
# else:
#     print('y is false') # if an int is zero
#
# parrot="Norwegian Blue"
# letter=input('Please enter some letters ')
# if letter in parrot:
#     print('{} was found in {}'.format(letter,parrot))
# else:
#     print('Invalid text')
# print('This is the end of Lecture 29')
#
# print()
# print('This is the beginning of Lecture 30')
# name=input('Please enter your name ')
# age=int(input('Please enter your age '))
# if 18< age <=30:
#     print('{} welcome to the holiday'.format(name))
# else:
#     print('{} are not eligible for the holiday'.format(name))
#
# print('This is the end of Lecture 30')

print('This is the beginning of Lecture 31')
printStr="4,220,123"
for i in range(0,len(printStr)):
    print('{} position has a value of {}'.format(i,printStr[i]))

cleanStr=''
for i in range(0,len(printStr)):
    if printStr[i] in '0123456789':
        cleanStr=cleanStr+printStr[i]
print(cleanStr)
print('This is the end of Lecture 31')

print()
print('This is the beginning of Lecture 32')
printStr32='3,456,789'
cleanStr32=''
for zz in printStr32:
    if zz in printStr32:
        cleanStr32=cleanStr32+zz
print(cleanStr32)
for i in range(0,50,3):
    print(i)

print('This is the end of Lecture 32')

