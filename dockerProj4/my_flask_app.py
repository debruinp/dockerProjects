# Import Flask. Import Flask class from the flask module. Flask is a popular web framework for Python that allows you to build web applications.

from flask import Flask

# Create a Flask app. Create an instance of the Flask class, passing the current module name (__name__) as an argument. 
# This is a common pattern in Flask, where the curent module name is used as the application's name.

my_flask_app = Flask(__name__)


# Define a route. This defines a route for the root URL (/) of the application.  The @app.route() decorator indicates that the function hello()
# should be executed when the root URL is accessed

@my_flask_app.route('/')
def hello():
    return 'Hey there, Docker!!!'


# Run the app. This is a common idiom in Python that checks if the script is being run directly (i.e., not being imported as a module by another script).
# If it is, the code inside the if block is executed. In this case, we use the app.run() method to start the Flask development server on:
# host='0.0.0.0': This allows the server to listen on all available network interfaces (not just localhost).
# port=5000: This sets the port number to 5000, which is a common choice for development servers.
# When you run this script, you should see the message 'Hello, Docker!' appear when you access http://localhost:5000/ in your web browser..
# ..(assuming you're running the script on your local machine).

if __name__ == '__main__':
    my_flask_app.run(host='0.0.0.0', port=5000)
