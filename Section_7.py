# Python Lists
country_list = ['America', 'Canada', 'Mexico', 'Germany', 'France']
index = 1
j=1

for country in country_list:
    print('{} country is '.format(index)+country)
    index += 1

country_list.append('India')
for country in country_list:
    print('{} country is '.format(j)+country)
    j += 1

# concatenating lists in python
even=[2, 4, 6, 8]
odd=[1,3,5,7]
allnumbers = even + odd
print('Even list + Odd List : {}'.format(allnumbers))
allnumbers.sort()  #  sort() method sorts the elements
# of the object allnumbers (of list type) without creating a new object
print('Sorted Even list + Odd List : {}'.format(allnumbers))

allNumbersSorted=sorted(allnumbers)
# sorted is a function that sorts the elements of the list and returns a new list object
print(allNumbersSorted)

list_1 = []
list_2 = list()  # When you call the List constructor with no arguments, an empty List is created

print('List_1 is : {}'.format(list_1))
print('List_2 is : {}'.format(list_2))

evenNumbers = [2,4,6,8]
another_evenNumbers = evenNumbers # both the objects another_evenNumbers and evenNumbers point to the
# same memory location that has the list [2,4,6,8]
print(evenNumbers is another_evenNumbers)
another_evenNumbers2 = list(evenNumbers)
print(another_evenNumbers2 is not evenNumbers)

even1 = [2, 4, 6, 8]
odd1 = [1, 3, 5, 7, 9]
numbers1=[even1, odd1] # we are creating a list called numbers1 that contains 2 lists namely even1 and odd1
print(numbers1)

for number_list in numbers1:
    print(number_list)

    for value in number_list:
        print(value)

print('!'*40)

string="2345"
my_iterator = iter(string)  # iter function returns an object of type string iterator
print(my_iterator)

list_1 = [2,4,6,'this is great']
my_iter2 = iter(list_1)
for item in my_iter2:
    print(item)

for i in range(0,len(list_1)):
    print(list_1[i])


print(range(10))

list_3 = list(range(10))
print(list_3)

list_even = list(range(0,10,2))
list_odd  = list(range(1,10,2))
list_odd.sort(reverse=True)
print(list_even+list_odd)

small_decimals = range(0,10,2)
print(small_decimals)
for j in small_decimals:
    print(j,'\t')
print(small_decimals.index(6))  # index function will return the position of the argument in the list


decimals = range(0,100)
print(decimals)

new_decimals=decimals[3:40:3]
print(new_decimals)
for i in new_decimals:
    print(i)

print(range(0,6,2) == range(0,5,2))
print(list(range(0,6,2)))
print(list(range(0,5,2)))

range_1=range(0,10,-2)
for i in range_1:
    print('Output of range(0,10,-2) is {}'.format(i)) # nothing is printed

range_2 = range(0,10)
for i in range_2[::-2]:  # this slicing reverses the values in range
    print(i)

o = range(0,100,4)
print(o)
p=o[::5]
print(p)
for i in p:
    print(i)

print('*'*40)

# Tuples are similar to lists . The difference is that tuples are immutable

t = ('a', 'b', 'c')
#t.append('s')

