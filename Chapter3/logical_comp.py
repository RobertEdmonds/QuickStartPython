"""Comparisons are the heart of every decision in programming"""
# if statements
a = "Yes"
# b = "Yes"
b = "No"
# At the end of the if statement we use a colon
if a == b:
    # There is no limit to the amount you can do if true
    print("A is equal to B")
    print("Really, it is, I promise")
else:
    print("A is not equal to B")
# else statements
one = 1
two = 2
three = 3
# elif is for else if
if one > two:
    print("One is greater than Two")
elif three < two:
    print("Three is less than Two")
else:
    print("None of these numbers are doing what we want")
# comparison symbols are called operators
if one > two:
    print("One is greater than Two")
    if two != three:
        print("but Two is not equal to Three")
    else:
        print("Two is equal to Three")
else:
    print("One is less than Two")
