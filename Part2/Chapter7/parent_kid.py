"""Parent and Child Classes"""
# First, let's define the Furniture class
class Furniture:
    """This is where all the furniture becomes a object"""
    def __init__(self, width = 0, height = 0, material = "Wood") -> None:
        self.width = width
        self.height = height
        self.material = material
# If I add an upgrade to the parent class the child class will receive it also
    # Upgrade = instance variable or new methods
# Next, let's define the Chair class
# The parentheses after the Class means it is a child of the class in the parentheses
class Chair(Furniture):
    """Chair Object"""
    def __init__(self, material, width = 0, height = 0, arms = True, back = True) -> None:
        # super is a short cut to the parent class
        # allows you to make uses of the parents class methods
        super().__init__(width, height, material)
        self.arms = arms
        self.back = back
# Expanding Child Classes
    def fold(self):
        """Register if the chair is folded"""
        self.folded = True
        print("The chair is folded")

    def unfold(self):
        """Register if the chair is unfolded"""
        self.folded = False
        print("The chair is unfolded")

# Multilevel Inheritance = When a class has a chain of ancestors
class Bench(Chair):
    """To show that bench is inheriting the chair instance"""
    pass
sofa = Bench("Metal")
print(vars(sofa))
# vars = very useful for testing and debugging
    # as long as it is an object for its argument returns the dictionary for the object in question

# Multiple Inheritance = Children of multiple parents share attributes of both parents
# Surface and Furniture are both parents
class Surface:
    """Tell us if the surface is flat"""
    def __init__(self, flat) -> None:
        self.flat = flat

class Table(Furniture, Surface):
    """Make a table object with using Furniture and Surface as parents"""
    def __init__(self, width=0, height=0, material="Wood", flat=True) -> None:
        # with two parents super() is not specific enough
        Furniture.__init__(self, width, height, material)
        Surface.__init__(self, flat)
        self.legs = 4
a = Table()
print(f"Table {vars(a)}")

# Introduction to Design Patterns
# Design Pattern
    # A structured way of solving a problem
    # Very useful technique when you have classes that share many things in common
# Default Arguments
    # makes production easier
    # only use keyword arguments
