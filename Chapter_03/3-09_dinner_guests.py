# Excercise 3-9 Dinner Guests
# Learning Objective: Utilize len() method on an earlier program. 

#Guest List Ex 3-4
guests = ['Tim', 'Steve', 'Aaron', 'Paul', 'Luke', 'Derek']

"""
print(f"Hi there {guests[0]} please come over for dinner!")
print(f"Hi there {guests[1]} please come over for dinner!")
print(f"Hi there {guests[2]} please come over for dinner!")
print(f"Hi there {guests[3]} please come over for dinner!")
print(f"Hi there {guests[4]} please come over for dinner!")
print(f"Hi there {guests[5]} please come over for dinner!")
"""

print("We are inviting " + str(len(guests)) + " guests.")
# str method hasn't been mentioned yet but given the sytax error provided, 
# it was needed to convert the int value to a string. 