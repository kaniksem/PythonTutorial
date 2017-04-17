print('this is the beginning of lecture 21')
print("hello world")
print(1+2)
print('We can even include "quotes" in strings')
print("You can even " + 'concatenate strings in Python')
print('this is the end of lecture 21 ')
#this is a python comment

print()
print('this is the beginning of lecture 22')
name = input('Please enter your name')
print('Hello' + ' ' + name)
print("This string has \nbeen split over \n several times")
tabbedString='1\t2\t3\t4\t'
print(tabbedString)
print('The pet owner said that "he\'s out of his mind"')
print("The pet owner said that \"he's out of his mind\"")
splitString="""Triple
quotes
are
used
in Python
for
spliting
strings
without using back-slash n"""
print(splitString)
print('this is the end of lecture 22')

print()
print('this is the beginning of lecture 23')
age=30
age2=20
# print('Your age is' + " " + age) - this would generate an error
print('Your age is ' + str(age))
a=14
b=10
print(a+b)
print(a / b)  # Divides a by b and returns a float
print(a//b)  # Divides a by b and returns an integer
print(a % b)

for i in range(3, 10):
    print(i)
print('this is the end of lecture 23')

print()
print('this is the beginning of lecture 24')
parrot='Norwegian Blue'
print(parrot[3])  # Prints the 4th letter since the string starts at index 0
# print(parrot[50])   IndexError: string index out of range
print('Negative 4: '+parrot[-4])
print('Start at index 1 and go upto 3 characters: '+parrot[1:3])  # this will print 3-1==2 characters starting at index 1
print(parrot[10:13])
print(parrot[0:6:3])
print('Hello '*4)
today="Sunday"
print("day" in today)
print("Friday" in today)
print('this is the end of lecture 24')

print()
print('this is the beginning of lecture 25')
age=50
print("My age is {0} years".format(age))

for i in range(1,11):
    print('For {0:2}, squared is {1:3}, cubed is {2:4}, squared-squared is {3:5}'.format(i*3,i**2,i**3,i**4))
print('Value of Pi is : {0:2.10}'.format(22/7))
print('this is the end of lecture 25')
