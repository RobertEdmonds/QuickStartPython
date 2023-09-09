"""Greeting to the program"""
# pylint: disable=broad-except
# pylint: disable=invalid-name
# Make a greeting function
# says hello world or a name if inputted
def greetings(name = "World"):
    """Greets the user"""
    return f"Well Hello, {name}!"

def write_file(data, filename):
    try:
        # write the file
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        print(e)
        return False
    return True
