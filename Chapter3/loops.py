"""This will be discussing the looping options with python"""
# Iteration = moving through a collection of data, like in a loop
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# For Loop with a list
# Contains the temporary variable(planet) and the data structure or range to iterate through
# Colon at the end of the for statement
for planet in planets:
    print(planet)

singular_word = ["student", "teacher", "room"]
for word in singular_word:
    # the next line of code is == word = word + "s"
    word += "s"
    print(word)
    # when the for loop is finished you can use an else statement
else:
    print("Done!")
# else code will not run if there is a break but will run once the for loop is finished

# For Loop with a range
# supply the range function in place of the data structure
for i in range(10):
    print(i)
# This supplies the function with the argument of 10
# Argument = is a value that we supply to a function

# For Loop with an enumerate
# Enumerate is to maintain the value with the index in a list
for index, value in enumerate(planets):
    print("Plant " + str(index + 1) + ": " + value)

# While loops
# While loops runs commands as long as a comparison evaluates to be true
# Evaluates = is the act of running a statement and obtaining a value
i = 0
while i < 10:
    print("while loop is at " + str(i))
    i += 1

bottles = 99
while bottles > 0:
    print(f"{bottles} bottles of beer on the wall.")
    print(f"{bottles} bottles of beer.")
    bottles -= 1
    print("Take one down, pass it around,")
    print(f"{bottles} bottles of beer on the wall.")

# Breaks in loops
# This would normally create an infinity loop, but not with the break
while True:
    print("Hello World!")
    break
# Your also able to break with an conditional
for i in range(10):
    print(i)
    if i > 5:
        break

# Continue in loops
# Continue allows us to skip the current iteration and move to the next without exiting the loop
# To pull out all the even numbers
for i in range(10):
    if i % 2:
        continue
    print(i)
# Modulo(mod for short) = performs a division operation on the variable and returns the remainder

# Nested loops
# loops can exist within themselves
for i in range(10):
    for j in range(10):
        print(f"{i}{j}")
