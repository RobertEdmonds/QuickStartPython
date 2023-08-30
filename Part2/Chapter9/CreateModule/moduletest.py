import distance
# pylint: disable=no-member

dist = distance.Distance(3)
print(f"{dist.km} kilometers is {dist.miles} miles")
dist.miles = (10)
print(f"{dist.miles} miles is {dist.km} kilometers")
