# Exercise 3-10 Every Function 
# Learning Objective: Use every function in the chapter at least once on a 
# custom list. 

'''
Functions introduced in the chapter: 
	1. listName.append('arg')
	2. listName.insert(index, 'value')
	3. del listName[index]
	4. listName.pop(index)
	5. listName.remove('value')
	6. listName.sort()
	7. listname.sort(reverse=True)
	8. sorted(listName)
	9. listName.reverse()
	10. len(listName)
'''

drinksList = ['Cofffe', 'Monster', 'Pepsi', 'Coke', 'Sprite', 'Dr. Pepper']

print("Original List: " + str(drinksList))

#1. append()
drinksList.append('Ginger Ale')

print("\n#1: append(): " + str(drinksList) + " ")

#2. insert()

drinksList.insert(1, 'Orange Soda')

print("\n#2: insert(): " + str(drinksList))

#3. del 
 
del drinksList[2]

print("\n#3. del: " + str(drinksList))

#4. pop()

drinksList.pop(0)

print("\n#4. pop(): " + str(drinksList))

#5. remove()

drinksList.remove('Coke')

print("\n#5. remove(): " + str(drinksList))

#6. sort()

drinksList.sort()

print("\n#6. sort(): " + str(drinksList))

#7. sort(reverse=True)

drinksList.sort(reverse=True)

print("\n#7. sort(reverse=True): " + str(drinksList))

drinksList.sort(reverse=True)

#8. sorted()

print("\n#8. sorted(): " + str(sorted(drinksList)))

#9. reverse()
drinksList.reverse()
print("\n#9. reverse(): " + str(drinksList))

#10. len() 

print("\n#10. len(): " + str(len(drinksList)))