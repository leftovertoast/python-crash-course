# Exercise 5-6 Stage of Life
# Learning Objective: write if-elif-else chain.

'''
# test
variable1 = '23'
if type(int(variable1)) == int:
    print(variable1)
else:
    print("Invalid")
'''
myAge = input('Please enter an age: ')

if type(int(myAge)) != int:
    print("\nYou've entered an invalid value. Exiting..")
elif int(myAge) < 2:
    print('\nThis person is just a baby.')
elif (int(myAge) >= 2) and (int(myAge) < 4):
    print('\nThis person is a toddler.')
elif (int(myAge) >= 4) and (int(myAge) < 13):
    print('\nThis person is a kid.')
elif (int(myAge) >= 13) and (int(myAge) < 20):
    print('\nThis person is a teenager.')
elif (int(myAge) >= 20) and (int(myAge) < 65):
    print('\nThis person is an adult')
elif int(myAge) >= 65:
    print('This person is an elder.')

# There's a better way to do this.

