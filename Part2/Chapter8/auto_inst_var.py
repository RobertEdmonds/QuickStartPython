"""Automatic Instance Variables"""
# Include the dataclasses module
from dataclasses import dataclass
# Define a new class
# without dataclass
# class Customer:
#     """This class is for Customer objects"""
#     def __init__(self, name, city) -> None:
#         self.name = name
#         self.city = city

# With dataclass
@dataclass
class Customer:
    """This class is for Customer objects"""
    name: str
    city: str = "Bailey"
    # to set default value do the type of variable = value
    bonus_points: int = 100
    total_spent: float = 0.00
    # rewrite eq method
    def __eq__(self, other) -> bool:
        # checks if other is a instance of Customer
            # with the isinstance variable
        if isinstance(other, Customer):
            # check if it works for name
            # return self.name == other.name
            # check if it works for city
            return self.city == other.city
        return False

@dataclass
class Person:
    """This class is for Customer objects"""
    name: str
    city: str = "Bailey"
    # to set default value do the type of variable = value
    bonus_points: int = 100
    total_spent: float = 0.00

    def __eq__(self, other) -> bool:
        if self.name == other.name:
            return True
        return False

c1 = Customer("Robert")
c2 = Customer("Holly")
p1 = Person("Robert")

print(repr(c1))
print(c1 == c2)
print(f"Customer eq method {c1 == p1}")
print(f"Person eq method {p1 == c1}")
