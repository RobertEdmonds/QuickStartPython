"""Modifying Arguments"""
# strongly advise against modifying arguments that is passed to a function
x = 5

def double(n):
    """Takes a integer and multiples it by two"""
    return n * 2
# modify the variable outside of the function
x = double(x)
print(x)
