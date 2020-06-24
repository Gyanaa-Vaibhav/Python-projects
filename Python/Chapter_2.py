# 2-1. Simple Message: Assign a message to a variable, and then
# print that message.
message = 'Hi my first and simple assinment'
print(message)

# 2-2. Simple Messages: Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print the new message.
new_message = 'Hi my first and simple assinment'
print(new_message)

# 2-3 Use a variable to represent a person’s name, and print a
# message to that person
eric = 'Hello Eric, would you like to learn some Python today?'

# 2-4 Use a variable to represent a person’s name, and then print that person’s name in lowercase,
# uppercase, and title case
Persons_name = 'ada loveace'

# 2-5 Find a quote from a famous person you admire. Print the quote
# and the name of its author.
print(Persons_name.upper())
print(Persons_name.lower())
print(Persons_name.title())

# 2-6 Repeat Exercise 2-5, but this time, represent the famous person’s name using a
# variable called famous_person. Then compose your message and represent it with a new
# variable called message. Print your message.
Famous_person = 'Albert Einstein'
message = f'{Famous_person} once said, "A person who never made\na mistake never tried anything new."'
print(message)

# 2-7 Use a variable to represent a person’s name, and include some
# whitespace characters at the beginning and end of the name.
Persons_name_2 = '\tMichle\tJackson\t'
print(Persons_name_2)

print('This is rstrip')
print(Persons_name_2.rstrip())
print('This is lstrip')
print(Persons_name_2.lstrip())
print('This is strip')
print(Persons_name_2.strip())

# 2-8 Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8.
print(5+3)
print(11-3)
print(2*4)
print(16/2)

# 2-9 Favorite Number: Use a variable to represent your favorite number. Then, using that
# variable, create a message that reveals your favorite number.
Fav_number = 6
print(f'My favourite number is {Fav_number}.')

# 2-10. Adding Comments: Choose two of the programs you’ve written, and
# add at least one comment to each.
# This Function Returns my name
def name():
    return 'Gyanaa'
print(name())

# 2-11. Zen of Python: Enter import this into a Python terminal session
# and skim through the additional principles.
import this
help(this)