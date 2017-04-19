print('This is the beginning of Lecture 28')
age=int(input("Please enter you age "))  # Converting string into int
if 18 <= age <= 34:
    print("You are a millenial")
elif age < 18:
    print("You are too young")
elif 35 <= age <= 50:
    print("You are Gen-X")
else :
    print("You are a baby-boomer")

print('This is the end of Lecture 28')

print()
print('This is the beginning of Lecture 29')
x=""
if x:
    print("x is true") # any non-empty value of this string will result in true
else:
    print("x is false") # if a string is empty then it is false
y=0
if y :
    print('y is true')  # any non-zero value of this int will result in true
else:
    print('y is false') # if an int is zero

parrot="Norwegian Blue"
letter=input('Please enter some letters ')
if letter in parrot:
    print('{} was found in {}'.format(letter,parrot))
else:
    print('Invalid text')
print('This is the end of Lecture 29')

print()
print('This is the beginning of Lecture 30')
name=input('Please enter your name ')
age=int(input('Please enter your age '))
if 18< age <=30:
    print('{} welcome to the holiday'.format(name))
else:
    print('{} are not eligible for the holiday'.format(name))

print('This is the end of Lecture 30')

print('This is the beginning of Lecture 31')
printStr = "4,220,123"
for i in range(0, len(printStr)):
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
# print(cleanStr32)
for i in range(0, 50, 3):
    print(i)

print('This is the end of Lecture 32')

print()
print('This is the beginning of Lecture 33 & 34')

shopping_list=["eggs", "bread", "spam", "bacon"]
for item in shopping_list:
    if item == "spam":
        # print("You cannot have {} for breakfast".format(item))
        continue
    else:
        print("Buy {}".format(item))

number="9,456,213,453,657,980,994,671"
cleanNumber=''

for i in range(0,len(number)):
    if number[i] in '0123456789':
        cleanNumber += number[i]   # this is known as AugmentedAssignment
print("Cleaned Number is : " + cleanNumber) # here cleanNumber is a string
print("Cleaned Number is : {}".format(cleanNumber))

print('This is the end of Lecture 33 & 34')

print()
print('This is the beginning of Lecture 35 & 36')

ipAddress=input("Please enter an IP address: ")
count=''

for i in range(0,len(ipAddress)):
    if (ipAddress[i] not in '.') and (ipAddress[i] not in '0123456789'):
        print("Please enter a valid IP address")
        break
    elif ipAddress[i] not in '0123456789':
        count += ipAddress[i]

if count is '':
    segments=0
else:
    segments=len(count)+1
print("There are {} segments in the IP Address".format(segments))

print('This is the end of Lecture 35 & 36')


print()
print('This is the start of Lecture 37 & 38')
i=0
while i < 10:
    print("{}".format(i))
    i+=1
print('This is the end of Lecture 37 & 38')


