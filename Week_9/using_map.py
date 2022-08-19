# to use map function it must be an iterable
a = [2,5,6,7,8,9]
def check_odd(a):
    return a % 2 != 0

print(list(filter(check_odd, a)))
#filter is used to filter a list
#you can use zip to agreegate different iterables, two or more
#lamda fuctions are used for functions taht are only used once
#map is used to carry out operations on a list
# sometimes 2 of these functions are used together 
#lambda can be used with other methods, when working with lambda you muat have a key

mylist = [ 2, 3, 4, 5, 6]

newlist = list(map(lambda num: num**2, mylist))
print(newlist)

b = [-1, -3, 4, 5, 6, 7, 2, -8 ]

b.sort(key = lambda y: y)
print(b)
