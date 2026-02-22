#create a tuple
abc= (1,'a','b',2 )
print(abc)
#create a tuple without a bracket
abc= 1, 2,'a','b', 3, 'c'
print(abc)
# Nested tuple
my_tuple= (1,'a',2, [3,4,'c'], ('hello', 9,'hi'))
print(my_tuple[4][0])
print(my_tuple[4][2][1])
#slicing
print(my_tuple[0:3])
print(my_tuple[-3:])
# print all the elements in the tuple using slicing
print(my_tuple[:])
#print all the elements but backwards
print(my_tuple[::-1])
#check if we can modify tuples
#my_tuple[0]=8
#print(my_tuple)
#But we can modify the list inside the tuple
my_tuple[3][2]= 'd'
print(my_tuple)
#packing the values
cde=('c',4,'d',5,'e')
print(cde)
#unpacking the values
a,b,c,y,o= cde
print(a)
print(b)
print(c)
print(y)
print(o)