# Ken Valverde
# 1527936s


# Exception handling to detect input string vs. integer

# Program will read a list of single-word names and ages (ending with -1)
# Then output that list with the age incremented.

# If a second input on a line is a string rather than an integer,
#   the program will throw an exception.

# Add try and except blocks to catch the ValueError exception and output 0 for the age.

#                                   0    1
# Split input to make a list >>> [name, age]
user_input = input().split()

# Index 0 of parts list will be the name.
name = user_input[0]

# While loop for user input until -1 is entered.
while name != '-1':
    try:
        # Index 1 of parts list will be the age and will increment by 1
        age = int(user_input[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(name, age))

    user_input = input().split()
    name = user_input[0]







