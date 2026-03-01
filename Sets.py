mylist=[1,4,2,3,1,7,2]
print(mylist)
myset=set(mylist)
print(myset)
#check if an element exists in a set
if 7 in myset:
    print(6)
else:
    print("No")
#How to add an element to a set
myset2= {1}
myset2.add(5)
myset2.add(3)
myset2.add(6)
myset2.add(5)
print(myset2)
#How to remove an element from a set
myset.remove(7)
print(myset)
#myset.remove(7) #if an element is not present in a set it throws an error
myset.discard(7)
print(myset)#Doesn't throw an error if element is not present
#set operations
set1={1,5,9,3}
set2={2,3,4,6}
#Union-> adding 2 sets together
print(set1.union(set2))
print(set1|set2)
#intersection->common elements
print(set1&set2)
#difference->elements that exist in the first set
print(set1-set2)
#symetric difference->union-intersection
print(set1^set2)