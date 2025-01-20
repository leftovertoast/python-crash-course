# Exercise 3-6 More Guests
# Learning Objective: Utitlize insert() & append() methods on a list to modify it. 


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

guests.insert(0, 'Joey')
guests.insert(3, 'Kate')
guests.append('Patti')

print(f"Hi there {guests[0]} please come over for dinner!")
print(f"Hi there {guests[1]} please come over for dinner!")
print(f"Hi there {guests[2]} please come over for dinner!")
print(f"Hi there {guests[3]} please come over for dinner!")
print(f"Hi there {guests[4]} please come over for dinner!")
print(f"Hi there {guests[5]} please come over for dinner!")
print(f"Hi there {guests[6]} please come over for dinner!")
print(f"Hi there {guests[7]} please come over for dinner!")


