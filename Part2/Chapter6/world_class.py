"""The Hello World Class, Object Lifecycle"""
# Define a world class
class World:
    """Make a class that has a greeting of hello world"""
    # Define our greeting
    greeting = "Hello, World!"

    # run this whenever the object is created
    def __init__(self) -> None:
        # print the greeting
        print(self.greeting)
# You can call on the class and the variable and it will show the variable
print(World.greeting)

# Use the class World to create a world object named w
w = World()

# Classes start with a capital letter
# Classes can have as many variables and methods as needed
# We are more focused on what the class produces -- objects
