"""Using the math module"""
import math
import datetime as DT
import statistics

# number = input("Pick a number: ")

# number = int(number)

# result = math.sqrt(number)

# print("The square root of {:n} is {:.2f}".format(number, result))
# print(f"The square root of {number} is {result}")

now = DT.datetime.now()
print(now)

numbers = [1, 4, 17, 62, 12, 84, 5, 8, 21]
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
stdev = statistics.stdev(numbers)
print(f"Mean: {mean} \n Median: {median} \n Mode: {mode} \n Standard Deviation: {stdev}")
