# Exercise 5-2 More Conditional Tests 
# Learning Objective: Write more conditional tests in specific fashions. 
	# a. test for equality of strings.
	# b. test using lower() method.
	# c. numerical test involving ==, <=, >=, <, >. 
	# d. test with 'and' & test with 'or' keywords.
	# e. test if item is in list.
	# f. test if item is not in list. 
'''
_ _ _ _ _ _ _ _ _ EXERCISE 5-1 _ _ _ _ _ _ _ _ _ _
coin = 'heads'
print("Is coin == 'heads'? I think so.")
print(coin == 'heads')

print("\nIs coin == 'tails'? I don't believe so.")
print(coin == 'tails')

color = 'black'
print("\nIs the color black?")
print(color == 'black')

print("\nIs the color 'white'?")
print(color == 'white')

coin = 'tails'
print("\nIs coin == 'heads'? I don't think so.")
print(coin == 'heads')

print("\nIs coin == 'tails'? I believe so.")
print(coin == 'tails')

color = 'white'
print("\nIs the color black?")
print(color == 'black')

print("\nIs the color 'white'?")
print(color == 'white')

lightSwitch = 'on'
print("\nIs the light on or off? I think its on.")
print(lightSwitch == 'on')

print("\nIs the light off? I don't think it is.")
print(lightSwitch == 'off')
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

'''
# String Equality Tests 

string1 = 'Welcome'
string2 = 'Goodbye'
print("Are string1 & string2 equal?")
print(string1 == string2)
print("\nAre string1 & string2 different?")
print(string1 != string2)

# Using lower() method 

string3 = 'Cheeks'
string4 = 'cheeks'

print("\nUsing lower are the names equal?")
print(string3.lower() == string4)

# Numerical tests <, >, <=, >=, ==

oneGig = 1024 
twoGig = 2048

print("\nTwo gigs is bigger than one:")
print(oneGig < twoGig)

print("\nOne gig is bigger than two gigs:")
print(oneGig > twoGig)

print("\nTwo gigs is bigger or equal to one gigs equal the same amount:")
print(twoGig >= oneGig)

print("\nTwo gigs is less than or equal to one gig:")
print(twoGig <= oneGig)

print("\nTwo gigs is equal to one gig:")
print(twoGig == oneGig)

# Tests with AND & OR keywords 

numOfPages = 77

print("\nThe number of pages is greater than 20 and also less than 100?")
print((numOfPages > 20) and (numOfPages < 100))

print("\nThe number of pages is either greater than 20 or less than 60?")
print((numOfPages > 20) or (numOfPages < 60))

# Test if item is in or not in list 

myList = ['banana', 'pineapple', 'apple', 'pear', 'strawberry', 'peach']
print(f"\nmyList = {myList}")

print("\nLet's test if PINEAPPLE is in our list:")
print('pineapple' in myList)

print("\nLet's now test if BLUEBERRY is in our list:")
print('blueberry' in myList)
