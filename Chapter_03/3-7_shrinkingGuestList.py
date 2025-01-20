# Exercise 3-7 Shrinking Guest List
# Learning Objective: Utitlize pop() and del methods to empty the list and inform guests. 


#Guest List Ex 3-4
guests = ['Tim', 'Steve', 'Aaron', 'Paul', 'Luke', 'Derek']

print(f"Hi there {guests[0]} please come over for dinner!")
print(f"Hi there {guests[1]} please come over for dinner!")
print(f"Hi there {guests[2]} please come over for dinner!")
print(f"Hi there {guests[3]} please come over for dinner!")
print(f"Hi there {guests[4]} please come over for dinner!")
print(f"Hi there {guests[5]} please come over for dinner!")

#Changing Guest list Ex 3-5
cantMakeIt = guests.pop(1)
print(f"Unfortunately {cantMakeIt} can't make it.")
print(f"Hi there {guests[0]} please come over for dinner!")
print(f"Hi there {guests[1]} please come over for dinner!")
print(f"Hi there {guests[2]} please come over for dinner!")
print(f"Hi there {guests[3]} please come over for dinner!")
print(f"Hi there {guests[4]} please come over for dinner!")

#More Guests Ex 3-6 
print("Hey we got a bigger table!")

guests.insert(0, 'Peter')
guests.insert(3, 'Karen')
guests.append('Perry')

print(f"Hi there {guests[0]} please come over for dinner!")
print(f"Hi there {guests[1]} please come over for dinner!")
print(f"Hi there {guests[2]} please come over for dinner!")
print(f"Hi there {guests[3]} please come over for dinner!")
print(f"Hi there {guests[4]} please come over for dinner!")
print(f"Hi there {guests[5]} please come over for dinner!")
print(f"Hi there {guests[6]} please come over for dinner!")
print(f"Hi there {guests[7]} please come over for dinner!")

#Shrinking Guest List 3-7
guestOut = guests.pop() 
print(f"Sorry {guestOut}, the dinner is cancelled")
guestOut = guests.pop()
print(f"Sorry {guestOut}, the dinner is cancelled")
guestOut = guests.pop()
print(f"Sorry {guestOut}, the dinner is cancelled")
guestOut = guests.pop()
print(f"Sorry {guestOut}, the dinner is cancelled")
guestOut = guests.pop()
print(f"Sorry {guestOut}, the dinner is cancelled")
guestOut = guests.pop()
print(f"Sorry {guestOut}, the dinner is cancelled")

print(f"Hey {guests[0]}, the dinner is still on, please join {guests[1]} and I.")
print(f"Hey {guests[1]}, the dinner is still on, please join {guests[0]} and I.")

del guests[1]
del guests[0] 

print(f"LIST: {guests}")