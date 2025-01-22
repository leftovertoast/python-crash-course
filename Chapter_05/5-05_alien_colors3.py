# Exercise 5-5 Alien Colors #3
# Learning Objective: Utilize if/elif/else statements, expanding on previous 2 programs.

# Version 1/2/3 = Alien Color is choosable.

alien_color = input('What is the alien color?')

if (alien_color == 'green'):
    print("\nPlayer has scored 5 points")
elif (alien_color == 'yellow'):
	print("\nPlayer has scored 10 points")
elif (alien_color == 'red'):
	print("\nPlayer has scored 15 points")
else:
	print("\nInvalid Input, please re-run the program!")