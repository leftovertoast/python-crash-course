# Exercise 4-12 More Loops
# Learning Objective: Use loops to rewrite a version of foods.py from Chapter 4

'''
foods.py
_ _ _ _ _ _ _

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
_ _ _ _ _ _ _
'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
	print(food)
print("\nMy friend's favorite foods are: ")
for food in friend_foods:
	print(food)

