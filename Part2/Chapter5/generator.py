"""Generator Functions"""
# Scope = the place where data structures and functions can be accessed

# Generator = runs until it reaches a yield statement
# def infinity():
#     """count up forever"""
#     i = 0
#     while True:
#         yield i
#         i += 1

# for i in infinity():
#     print(i)
def bottles_song(start = 1, end = 99):
    """Sings the bottles of beer on the wall"""
    # Set the initial number of bottles to the start argument
    bottles = start
    # Loop through until bottles are gone
    while bottles < end:
        # Display the song
        # Verse becomes our buffer(a place to temporarily store data)
        verse = f"{bottles} bottles of beer on the wall. "
        verse += f"{bottles} bottles of beer. "
        verse += "Take one down, pass it around, "
        # Subtract a bottle
        bottles += 1
        verse += f"{bottles} bottles of beer on the wall."
        # Yield to the calling functions
        yield verse
        # Pick back up here when we return
    # return True

# Loop through the generator
for i in bottles_song(end=6):
    print(i)
