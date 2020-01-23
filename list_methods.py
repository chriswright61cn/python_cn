mylist = [
    'list_item41',
    'list_item03',
    'list_item112',
    'list_item14',
    'list_item25',
    'list_item1'
]
print(mylist)

#sort()
# sorts original list
mylist.sort()
print(mylist)

#sort(reverse=True)
# reverse sorts original list
mylist.sort(reverse=True)
print(mylist)

# remove()
# removes named element
mylist.remove('list_item1')
print(mylist)

# reverse()
# reverses original list
mylist.reverse()
print(mylist)

# count() occurance of an element in a  list
print(mylist.count('list_item1'))

# extend() add two lists
# List1.extend(List2)
mylist.extend(['listitem_6','listitem_7'])
print(mylist)

# insert()at a position
# list.insert(<position, element)
mylist.insert(2,'Cuckoo')
print(mylist)

mylist.sort()
print(mylist)

mylist.clear()
print(mylist)

mylist.extend([1,5,2,56,23,75,35,85,23])
print(mylist)

mylist.sort()
print(mylist)

mylist.pop(4)
print(mylist)

