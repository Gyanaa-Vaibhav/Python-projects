# 3-1. Names: Store the names of a few of your friends in a
# list called names. Print each person’s name by accessing each element in the list, one at a time.
Friends = ['Gyanaa', 'Vaibhav']
print(Friends[0])
print(Friends[1])

# 3-2. Greetings: Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name, print a message to them.
print(f'Hi how are you {Friends[0]}')
print(f'Hi how are you {Friends[1]}')

# 3-3. Your Own List: Think of your favorite mode of transportation,
# such as a motorcycle or a car, and make a list that stores several examples.
Transportation = ['car', 'bike', 'Motorcycel']
print(f"I would like to own a Honda {Transportation[1]}.")
print(f'I would like to own a Honda {Transportation[2]}')
print(f'I would like to own a Honda {Transportation[0]}')

# 3-4. Guest List: If you could invite anyone, living or deceased
# to dinner, who would you invite? Make a list that includes at
# least three people you’d like to invite to dinner and print their name
Guest_list = ['Nmae1', 'Name2', 'Name3', 'Name4']
print(f'Hi {Guest_list[0]} i invite you to my dinner')
print(f'Hi {Guest_list[1]} i invite you to my dinner')
print(f'Hi {Guest_list[2]} i invite you to my dinner')
print(f'Hi {Guest_list[3]} i invite you to my dinner')

# 3-5. Changing Guest List: You just heard that one of your guests
# can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
del Guest_list[1:3]

print(Guest_list)
Updates_list = ['Name5','Nmae6','Name7']
