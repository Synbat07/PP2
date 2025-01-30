#LISTS

thislist = ["apple", "banana", "cherry"]
print(thislist)

#1) Access Items
thislist = ["apple", "banana", "cherry"]
print ("1) ")
print (thislist[1])

#2) Change List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print("2) ", (thislist))

#3) Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print("3) ", (thislist))

#4) Remove List Items (1 - remove; 2 - pop; 3 - del)
#4.1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(("4.1) ", thislist))

#4.2
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print("4.2) ", (thislist))
#удаляет последний элемент

#4.3
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("4.3) ", (thislist))


#5) Loop Lists
thislist = ["apple", "banana", "cherry"]
print ("5)")
for x in thislist:
  print (x)
  
#6) Sort Lists
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print("6) ", (thislist))

#7) Join Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print ("7) ")
print(list1)
