"""This is to access SQLite Database"""
# import sqlite3 module
import sqlite3

# Create a db object by connecting to the sTunes.db database
db = sqlite3.connect("sTunes.db")

# run query
query = "select * from tracks"

for row in db.execute(query):
    print(row)
    