"""Mopping Up the Mess with Finally"""
# finally block is executed even if an exception is raised in the code protected by try
    # finally block runs no matter what

# Divide a number by zero
a = 7
b = 0

try:
    print(f"{a} divided by {b} is {a / b}")
except Exception as e:
    print(f"It didn't work because of {e}")
finally:
# should use conditional to restore sanity to the program
    print("But we tried!")

print("All done!")
