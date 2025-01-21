# Exercise 4-12 Buffet
# Learning Objective: Use tuple, list it with for loop and reassign it. 

buffetFoods = ('carrots', 'potatoes', 'salad', 'beef', 'chicken')
print("The buffet offers the following foods:")
for food in buffetFoods:
	print(food)
#try to modify to ensure error shows up: 
# buffetFoods[3] = 'pork' ---> Confirmed error raised 

#menu changed: 
buffetFoods = ('carrots', 'string beans', 'corn', 'beef', 'chicken')
print("\nThe buffet now offers the following foods: ")
for food in buffetFoods:
	print(food)
