"""Using exceptions in Python"""
# Exceptions = used to describe code that executes in some abnormal way
# try: Try to run this code
    # except: Run this code when something goes wrong
    # else: Everything went fine, so run this
# finally: No matter what happens, run this code

# Divide a number by zero
a = 7
b = 0
# code after try: and its companion except:
try:
    print(f"{a} divided by {b} is {a / b}")
# it is not recommended to catch all errors with the except
    # specify which errors your looking for
# OverflowError = occurs when the resulting answer to a math problem is too large to store
# except OverflowError as e:
# ZeroDivisionError = When a number is divided by zero
except ZeroDivisionError as e:
# Exception = If we are unsure of the exception it might through
    # printing the e will give you an idea of which exception to add
# except Exception as e:
    print(f"Something went wrong dividing these numbers\n{e}?\n")
# have to turn the e into a string or you'll get an error because e is an error class
print("All done!")
