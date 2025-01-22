# Exercise 3-5 Changing Guest List
# Learning Objective: Remove an item from a list utilizing pop() method.


#Guest List Ex 3-4
guests = ['Tim', 'Steve', 'Aaron', 'Paul', 'Luke', 'Derek']

print(f"Hi there {guests[0]} please come over for dinner!")
print(f"Hi there {guests[1]} please come over for dinner!")
print(f"Hi there {guests[2]} please come over for dinner!")
print(f"Hi there {guests[3]} please come over for dinner!")
print(f"Hi there {guests[4]} please come over for dinner!")
print(f"Hi there {guests[5]} please come over for dinner!")

#Changing Guest List Ex 3-5
cantMakeIt = guests.pop(1)
print(f"Unfortunately {cantMakeIt} can't make it.")
print(f"Hi there {guests[0]} please come over for dinner!")
print(f"Hi there {guests[1]} please come over for dinner!")
print(f"Hi there {guests[2]} please come over for dinner!")
print(f"Hi there {guests[3]} please come over for dinner!")
print(f"Hi there {guests[4]} please come over for dinner!")



