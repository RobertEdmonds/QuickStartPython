"""Instance Variables, Scope in Classes"""
# example
class Customer:
    """Class for naming customers"""
    def __init__(self, name, city) -> None:
        self.name = name
        self.city = city
    # init is creating a new object

    def __enter__(self):
        print("Entering Scope.")
        # Run code upon entering scope of with statement
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving scope.")
        # Run code upon leaving scope of with statement

    def greet(self):
        # self is the variable you are calling it on
        """Says hello to new customers"""
        print(f"Hello, {self.name}!")


# Create three objects based on the Customer Class
c1 = Customer(name="Bobby", city="Littleton")
c2 = Customer(city="Bailey", name="Robert")
c3 = Customer(name="Rob", city="Naples")
# Instance Variable = a variable defined within a class that is specific to that instance
    # in other words, specific to that object
customers = [c1, c2, c3]

for c in customers:
    c.greet()
    print(f"{c.name} lives in {c.city}!")

with Customer("Robert", "Colorado") as robert:
    robert.greet()

# __init__
    # init method is automatically called whenever an object is created from a class
    # Arguments passed at the objects creation will be available in init
        # declared after the self argument in the method definition

# __enter__ and __exit__
    # with statement calls the enter
    # makes use of a resource that we create
        # like an open file
    # must have a exit if you have an enter
    # temporary because this object is created inline by the with statement
        # once complete it will be gone
    # once the with statement is finished it calls the exit
        # Arguments for exit = self, exc_type, exc_value, traceback
            # exc_type, exc_value, traceback populate with values if an exception occurs

# __del__
    # Deletes objects we no longer need
    # Deleting objects is permanent
