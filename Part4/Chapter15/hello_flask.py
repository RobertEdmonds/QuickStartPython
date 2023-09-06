"""This is for the flask example"""
# import Flask
import json
from flask import Flask

# Create the app object
app = Flask(__name__)

# Create a menu dictionary
menu = {
    "name": "Hot Chocolate",
    "price": 3.99
}

# Convert to JSON
menu_json = json.dumps(menu)

# Define the hello function, with route decorator
@app.route("/")
def hello():
    return f"{menu_json}"

@app.route("/menu")
def main_menu():
    menu_price = menu_json.split(",")[1].split(":")[1].replace("}", "")
    return f"<h1>{menu_json}</h1> \n <h3>${menu_price}</h3>"
