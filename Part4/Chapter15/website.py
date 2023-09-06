"""This how to use web.py"""
# import web.py
import web

# Define the routes web.py will respond to
routes = (
    "/(.*)", "home"
)

# Create app object, providing routes and globals as arguments
app = web.application(routes, globals())

# Define the home class which will respond to our default route
class home:
    # Method to respond to GET requests
    def GET(self, name):
        """Responds to get request for the home class"""
        # Tell the browser we are sending HTML
        web.header("Content-Type", "text/html")
        # Set name to "World" if name not set
        if not name:
            name = "World"
        # return string to display
        return "<h1>Hello, " + name + "!</h1>"

# Make sure we are in the main program scope, then run!
if __name__ == "__main__":
    app.run()
