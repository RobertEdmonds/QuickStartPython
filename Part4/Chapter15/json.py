"""Converting Data to JSON"""
# import json
import json

# Create a menu dictionary
menu = {
    "name": "Hot Chocolate",
    "price": 3.99
}

# Convert to JSON
menu_json = json.dumps(menu)

# Display JSON
print(menu_json)

# Sample JSON retrieved via API POST (note the single quotes)
sample_json = '{"name": "Hot Chocolate", "price": 3.99}'

# Convert from JSON into Python dictionary
r_menu = json.loads(sample_json)

# Display menu dictionary
print(r_menu)
