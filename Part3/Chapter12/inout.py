"""Reading and writing files"""
# String to write
data = "The lazy red fox slept instead of jumping over a dog."

# Write the data
with open("fox.txt", mode="w", encoding="utf-8") as f:
    f.write(data)

# Read the file
with open("fox.txt", mode="r", encoding="utf-8") as f:
    read_data = f.read()

with open("fox.txt", mode="r", encoding="utf-8") as f:
    part_read = f.read(16)

# Display results
print("Original: " + data)
print("From Disk: " + read_data)
print("Partial Read: " + part_read)

import sys

# Read stdin into data-in
data_in = sys.stdin.read()

# Write to stdout
bytes_written = sys.stdout.write(data_in)

# Display stats
print(f"Wrote {bytes_written} bytes to stdout.")

import pickle

customer_names = ["Jim Smith", "Amber Dobson", "Al James"]

with open("customer.dat", mode="wb") as f:
    pickle.dump(customer_names, f)

with open("customer.dat", mode="rb") as f:
    load_data = pickle.load(f)

print("Original: " + str(customer_names))
print("Loaded: " + str(load_data))
