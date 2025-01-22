# Exercise 4-11 My Pizzas 
# Learning Objective: Copy a list and add to it making sure it is independant of the original list.


favoritePizzas = ['Meat lovers', 'White with Spinach and Feta', 'Pepperoni']

friendPizzas = favoritePizzas[:]

favoritePizzas.append('Chicken Parmesean')

friendPizzas.append('Hawaiian')

print(f"My favorite pizzas are: {favoritePizzas}.\n")

print(f"My friend's favorite pizzas are: {friendPizzas}.\n")

