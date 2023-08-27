"""Properties and Private Variables"""
# Convert kilometers to miles
class Converter:
    """Converts measurements"""
    def __init__(self, km) -> None:
        self.km = km

    def to_miles(self):
        """Converts kilometers to miles"""
        return self.km / 1.609

distance1 = Converter(3)
print(distance1.to_miles())

class Distance:
    """Converts distance measurement"""
    def __init__(self, km) -> None:
        # the under score in front of km makes it a private variable
            # Only accessible in the class
        self._km = km
    @property
    def km(self):
        """Stores the km"""
        return self._km
    # property is a decorator
        # Decorator = tells python to treat it more as a variable than a function
    @km.setter
    def km(self, value):
        self._km = value

    @property
    def miles(self):
        """Converts kilometers to miles"""
        return self._km / 1.609
    # Once something is a property we can set a setter
        # Setter = a property that sets a value internal to the object
    @miles.setter
    def miles(self, value):
        self._km = value * 1.609

distance2 = Distance(3)
print(f"{distance2.km} kilometers is {distance2.miles} miles.")
distance2.miles = 3
print(f"{distance2.km} kilometers is {distance2.miles} miles.")

class Length:
    """Converts Lengths"""
    def __init__(self, inch) -> None:
        self._inch = inch

    @property
    def inches(self):
        """gives access to the private variable _inch"""
        return self._inch

    @inches.setter
    def inches(self, value):
        self._inch = value

    @property
    def cm(self):
        """Converts Inches to Centimeters"""
        return self._inch * 2.54

    @cm.setter
    def cm(self, value):
        self._inch = value / 2.54

measurement1 = Length(4)
print(f"{measurement1.inches} inches is {measurement1.cm} centimeters.")
measurement1.cm = 36
print(f"{measurement1.inches} inches is {measurement1.cm} centimeters.")
